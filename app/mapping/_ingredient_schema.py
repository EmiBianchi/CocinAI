from marshmallow import fields, Schema, post_load
from app.models import Ingredient

class IngredientSchema(Schema):
    # Define la estructura para serializar y deserializar objetos Ingredient
    id = fields.Integer(dump_only=True)  # Solo para serialización
    name = fields.String(required=True, validate=fields.Length(max=50))  # Nombre del ingrediente, obligatorio y máximo 50 caracteres
    unit_measurement = fields.String(required=True, validate=fields.Length(max=20))  # Unidad de medida, obligatoria y máximo 20 caracteres
    recipes = fields.Nested('RecipeSchema', many=True, exclude=('ingredients',))  # Relación con recetas, evitando referencia circular

    @post_load
    def make_ingredient(self, data, **kwargs):
        # Crea una instancia de Ingredient después de la deserialización
        return Ingredient(**data)
