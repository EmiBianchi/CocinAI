from marshmallow import fields, Schema, post_load
from app.models import RecipeIngredient

class RecipeIngredientSchema(Schema):
    # Define la estructura para serializar y deserializar objetos RecipeIngredient
    recipe_id = fields.Integer(required=True)  # ID de la receta, obligatorio
    ingredient_id = fields.Integer(required=True)  # ID del ingrediente, obligatorio
    quantity = fields.Float(required=True)  # Cantidad del ingrediente, obligatorio
    ingredient = fields.Nested('IngredientSchema', only=('id', 'name', 'unit_measurement'))  # Datos del ingrediente

    @post_load
    def make_recipe_ingredient(self, data, **kwargs):
        # Crea una instancia de RecipeIngredient después de la deserialización
        return RecipeIngredient(**data)