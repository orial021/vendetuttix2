#se usa con python3 CRUDFactory.py
#Debe estar hecho el modelo antes de usarlo
#Se debe cambiar las variables CRUD y schema_class
#si hay algun enum se debe corregir en schema


import os

CRUD: str = "departament"
schema_class= "Departament"
properties_by_model = {}
properties_all_by_model = {}
model_name : str
service_name : str

def find_property_models(directory):
    for root, _, files in os.walk(directory):
        for model in files:
            if model.endswith("_model.py"):
                if model[:-9] == CRUD:
                    filepath = os.path.join(root, model)
                    with open(filepath, "r", encoding="utf-8") as file:
                        content = file.read()
                        inside_class = False
                        for line in content.splitlines():
                            if "(Model)" in line:
                                model_name = model[:-9]
                                inside_class = True
                            elif inside_class and "=" in line and model_name == CRUD:
                                property_all = line.split("Field")[0].strip()
                                property_name = line.split("=")[0].strip()
                                if property_name not in ["created_at", "updated_at", "deleted_at"]:
                                    properties_by_model.setdefault(model_name, []).append(property_name)
                                if property_all not in ["created_at = fields.Datetime", "updated_at = fields.Datetime", "deleted_at = fields.Datetime"]:
                                    field_type = property_all.split(".")[1].strip()
                                    properties_all_by_model.setdefault(model_name, []).append((property_name, field_type))
                            elif "def" in line:
                                inside_class = False
             
    return model_name, properties_all_by_model

def map_tortoise_field_to_pydantic_type(tortoise_field_type):
    """
    Mapea los tipos de campo de Tortoise ORM a los tipos correspondientes en Pydantic.
    """
    if "CharEnum" in tortoise_field_type:
        return "Enum"
    elif "Char" in tortoise_field_type or "Text" in tortoise_field_type:
        return "str"
    elif "Int" in tortoise_field_type:
        return "int"
    elif "Boolean" in tortoise_field_type:
        return "bool"
    
    else:
        return "str"

def convert_types_in_properties(properties_all_by_model):
    converted_properties = {}
    for model_name, properties in properties_all_by_model.items():
        converted_properties[model_name] = []
        for prop, field_type in properties:
            print(field_type)
            pydantic_type = map_tortoise_field_to_pydantic_type(field_type)
            print(pydantic_type)
            converted_properties[model_name].append((prop, pydantic_type))
    return converted_properties
    
def create_schema_file(model_name, converted_properties):
    output_directory = f"./schemas"
    os.makedirs(output_directory, exist_ok=True)
    schema_filename = os.path.join(output_directory, f"{model_name}_schema.py")  
    global service_name
    service_name = model_name
    with open(schema_filename, "w", encoding="utf-8") as schema_file:
        schema_file.write(f"from enum import Enum\nfrom pydantic import BaseModel\nfrom typing import Optional\nfrom datetime import datetime\n\n")
        schema_file.write(f"class {schema_class}(BaseModel):\n")
        for prop, _ in converted_properties.get(model_name, []):
            schema_file.write(f"    {prop}: {_}\n")
        schema_file.write("\n\n    model_config = { \n       'json_schema_extra':{\n            'example':{\n")
        for prop, _ in converted_properties.get(model_name, []):
            if _ == "int":
                exm = "1"
                schema_file.write(f"                '{prop}':{exm},\n")
            elif _ == "str":
                exm = "string"
                schema_file.write(f"                '{prop}':'{exm}',\n")
            elif _ == "bool":
                exm = "True"
                schema_file.write(f"                '{prop}':'{exm}',\n")
            else:
                schema_file.write(f"                '{prop}':'Other',\n")
        schema_file.write("            }\n        }\n    }\n\n")
        
        
        schema_file.write(f"class {schema_class}CreateSchema(BaseModel):\n")
        for prop, _ in converted_properties.get(model_name, []):
            if prop != "id":
                schema_file.write(f"    {prop}: {_}\n")
        schema_file.write("\n\n    model_config = { \n       'json_schema_extra':{\n            'example':{\n")
        for prop, _ in converted_properties.get(model_name, []):
            if prop != "id" and _ == "int":
                exm = "1"
                schema_file.write(f"                '{prop}':{exm},\n")
            elif prop != "id" and _ == "str":
                exm = "string"
                schema_file.write(f"                '{prop}':'{exm}',\n")
            elif prop != "id" and _ == "bool":
                exm = "True"
                schema_file.write(f"                '{prop}':'{exm}',\n")
            elif prop != "id" and _ != "int" and _ != "str" and _ != "bool":
                exm = "Other"
                schema_file.write(f"                '{prop}':'{exm}',\n")
        schema_file.write("            }\n        }\n    }\n\n")
        
        
        schema_file.write(f"class {schema_class}ResponseSchema({schema_class}CreateSchema):\n    id: int\n    created_at: datetime\n    updated_at: datetime\n    deleted_at: datetime | None = None\n")
        schema_file.write("\n\n    model_config = { \n       'json_schema_extra':{\n            'example':{\n")
        for prop, _ in converted_properties.get(model_name, []):
            if _ == "int":
                exm = "1"
                schema_file.write(f"                '{prop}':{exm},\n")
            elif _ == "str":
                exm = "string"
                schema_file.write(f"                '{prop}':'{exm}',\n")
            elif _ == "bool":
                exm = "True"
                schema_file.write(f"                '{prop}':'{exm}',\n")
            else:
                schema_file.write(f"                '{prop}':'Other',\n")
        schema_file.write("            }\n        }\n    }\n\n")       
    print(f"Archivo de esquema '{schema_filename}' creado exitosamente.")
    
def create_service_file(model_name, schema_class):
    output_directory = f"./services"
    os.makedirs(output_directory, exist_ok=True)
    schema_filename = os.path.join(output_directory, f"{model_name}_service.py")  
    with open(schema_filename, "w", encoding="utf-8") as schema_file:
        schema_file.write(f"from typing import Type, TypeVar, Generic\nfrom pydantic import BaseModel\nfrom tortoise.models import Model\nfrom datetime import datetime\nfrom schemas.{model_name}_schema import {schema_class}CreateSchema\nfrom models.{model_name}_model import {schema_class}\n\nT = TypeVar('T', bound=BaseModel)\nM = TypeVar('M', bound=Model)\n\n")
        
        schema_file.write(f"class CRUDService(Generic[T, M]):\n    def __init__(self, model: Type[M], schema: Type[T]):\n        self.model = model\n        self.schema = schema\n\n    async def create(self, data: T):\n        return await self.model.create(**data.model_dump())\n\n    async def get_all(self):\n        return await self.model.all()\n\n    async def get_by_id(self, id: int):\n        return await self.model.get_or_none(id=id)\n\n    async def update(self, id: int, data: T):\n        instance = await self.get_by_id(id)\n        if instance:\n            await instance.update_from_dict(data.model_dump()).save()\n            return instance\n        return None\n\n    async def delete(self, id: int):\n        instance = await self.get_by_id(id)\n        if instance:\n            instance.deleted_at = datetime.now()\n            await instance.save()\n            return instance\n        return None\n\n")
        
        schema_file.write(f"class {schema_class}Service(CRUDService[{schema_class}CreateSchema, {schema_class}]):\n    pass\n\n{model_name}_service = {schema_class}Service({schema_class}, {schema_class}CreateSchema)\n")
        
def create_controller_file(model_name, schema_class):
    output_directory = f"./controllers"
    os.makedirs(output_directory, exist_ok=True)
    schema_filename = os.path.join(output_directory, f"{model_name}_controller.py")  
    with open(schema_filename, "w", encoding="utf-8") as schema_file:
        schema_file.write(f"from services.{model_name}_service import {model_name}_service\nfrom schemas.{model_name}_schema import {schema_class}CreateSchema\nfrom fastapi import HTTPException\n\nasync def create_controller(data: {schema_class}CreateSchema):\n    return await {model_name}_service.create(data)\n\nasync def get_all_controller():\n    return await {model_name}_service.get_all()\n\nasync def get_controller(id: int):\n    {model_name} = await {model_name}_service.get_by_id(id)\n    if {model_name} is None:\n        raise HTTPException(status_code=404, detail='not found')\n    return {model_name}\n\nasync def update_controller(id: int, data: {schema_class}CreateSchema):\n    {model_name} = await {model_name}_service.update(id, data)\n    if {model_name} is None:\n        raise HTTPException(status_code=404, detail='not found')\n    return {model_name}\n\nasync def delete_controller(id: int):\n    {model_name} = await {model_name}_service.delete(id)\n    if {model_name} is None:\n        raise HTTPException(status_code=404, detail='not found')\n    return {model_name}")

def create_router_file(model_name, schema_class):
    router = f"{model_name}_router"
    output_directory = f"./routers"
    os.makedirs(output_directory, exist_ok=True)
    schema_filename = os.path.join(output_directory, f"{model_name}_router.py")  
    with open(schema_filename, "w", encoding="utf-8") as schema_file:
        schema_file.write(f"from typing import List\nfrom fastapi import APIRouter, Depends\nfrom models.user_model import User\nfrom schemas.{model_name}_schema import {schema_class}CreateSchema, {schema_class}ResponseSchema\nfrom controllers.{model_name}_controller import create_controller, get_all_controller, get_controller, update_controller, delete_controller\nfrom routers.user.auth_router import require_admin\n\n{router} = APIRouter()\n\n@{router}.get('/all', tags=['{schema_class}'], response_model=List[{schema_class}ResponseSchema])\nasync def all():\n    return await get_all_controller()\n\n@{router}.get")
        
        schema_file.write("('/show/{id}', ")
    
        schema_file.write(f"tags=['{schema_class}'], response_model={schema_class}ResponseSchema)\nasync def show(id: int):\n    return await get_controller(id)\n\n@{router}.post('/create', tags=['{schema_class}'], response_model={schema_class}ResponseSchema)\nasync def creater(data: {schema_class}CreateSchema, admin_user: User = Depends(require_admin)):\n    return await create_controller(data)\n\n@{router}.")
        
        schema_file.write("put('/update/{id}',")
        
        schema_file.write(f" tags=['{schema_class}'], response_model={schema_class}ResponseSchema)\nasync def updater(id: int, data: {schema_class}CreateSchema, admin_user: User = Depends(require_admin)):\n    return await update_controller(id, data)\n\n@{router}.")
        
        schema_file.write("delete('/delete/{id}',")
        
        schema_file.write(f" tags=['{schema_class}'], response_model={schema_class}ResponseSchema)\nasync def deleter(id: int, admin_user: User = Depends(require_admin)):\n    return await delete_controller(id)")





if __name__ == "__main__":
    directory = "./models"
    model_directory = "../models"
    name, props = find_property_models(directory)
    print(props)
    converted_properties =convert_types_in_properties(properties_all_by_model)
    create_schema_file(name, converted_properties)
    create_service_file(service_name, schema_class)
    create_controller_file(service_name, schema_class)
    create_router_file(service_name, schema_class)
