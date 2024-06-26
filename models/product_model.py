from tortoise import fields
from tortoise.models import Model


class Product(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    short_description = fields.CharField(max_length=100)
    long_description = fields.TextField(null=True)
    price = fields.FloatField()
    promo_price = fields.FloatField()
    init_promotional_date = fields.DatetimeField(null=True)
    end_promotional_date = fields.DatetimeField(null=True)
    tax = fields.FloatField()
    quantity = fields.IntField()
    is_active = fields.BooleanField()
    is_featured = fields.BooleanField()
    is_new = fields.BooleanField()
    category_id = fields.ForeignKeyField('models.Category', name='products')
    category = fields.CharField(max_length=50)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null = True)

    def __str__(self):
        return self.name
    
    class Meta:
        table = "product"
        
        
'''@app.get("/usuarios/{usuario_id}/items")
async def get_items(usuario_id: int):
    usuario = await Usuario.get(id=usuario_id)
    items = usuario.items
    return {"items": items}'''