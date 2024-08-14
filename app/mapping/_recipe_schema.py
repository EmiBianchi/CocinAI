from marshmallow import fields, Schema, post_load
from app.models import Recipe

class RecipeSchema(Schema):
    # Define la estructura para serializar y deserializar objetos Recipe
    id = fields.Integer(dump_only=True)  # Solo para serialización
    title = fields.String(required=True, validate=fields.Length(max=100))  # Título de la receta, obligatorio y máximo 100 caracteres
    instructions = fields.String(required=True)  # Instrucciones de la receta, obligatorias
    preparation_time = fields.Integer(required=True)  # Tiempo de preparación en minutos, obligatorio
    ingredients = fields.Nested('RecipeIngredientSchema', many=True)  # Relación con ingredientes de la receta
    diets = fields.Nested('DietSchema', many=True, only=('id', 'name'))  # Relación con dietas, solo incluyendo id y nombre

    @post_load
    def make_recipe(self, data, **kwargs):
        # Crea una instancia de Recipe después de la deserialización
        return Recipe(**data)