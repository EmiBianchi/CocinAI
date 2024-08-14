from marshmallow import fields, Schema, post_load
from app.models import Diet

class DietSchema(Schema):
    # Define la estructura para serializar y deserializar objetos Diet
    id = fields.Integer(dump_only=True)  # Solo para serialización, no se usa al crear nuevos objetos
    name = fields.String(required=True, validate=fields.Length(max=50))  # Nombre de la dieta, obligatorio y máximo 50 caracteres
    recipes = fields.Nested('RecipeSchema', many=True, exclude=('diets',))  # Relación con recetas, excluyendo la referencia circular a dietas

    @post_load
    def make_diet(self, data, **kwargs):
        # Crea una instancia de Diet después de la deserialización
        return Diet(**data)
    