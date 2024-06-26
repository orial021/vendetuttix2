from tortoise import fields
from tortoise.models import Model


class Category(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    description = fields.TextField()
    departament_id = fields.CharField(max_length=50)
    departament = fields.ForeignKeyField('models.Departament', related_name='categories')
    is_active = fields.BooleanField()
    image_url = fields.CharField(max_length=255, null=True)
    
    
    
    
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null = True)

    def __str__(self):
        return self.title
    
    class Meta:
        table = "category"