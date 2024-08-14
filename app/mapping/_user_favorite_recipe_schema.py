from marshmallow import fields, Schema, post_load
from app.models import UserFavoriteRecipe

class UserFavoriteRecipeSchema(Schema):
    # Define la estructura para serializar y deserializar objetos UserFavoriteRecipe
    id = fields.Integer(dump_only=True)  # Solo para serialización
    recipe_id = fields.Integer(required=True)  # ID de la receta favorita, obligatorio
    user_id = fields.Integer(required=True)  # ID del usuario, obligatorio
    recipe = fields.Nested('RecipeSchema', exclude=('user_favorite_recipe',))  # Datos de la receta, excluyendo la referencia circular

    @post_load
    def make_user_favorite_recipe(self, data, **kwargs):
        # Crea una instancia de UserFavoriteRecipe después de la deserialización
        return UserFavoriteRecipe(**data)