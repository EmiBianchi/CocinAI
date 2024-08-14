from flask import Blueprint, request
from app.mapping import UserFavoriteRecipeSchema, ResponseSchema 
from app.services.response_message import ResponseBuilder
from app.services.user_favorite_recipe_services import UserFavoriteRecipeService

user_favorite_recipe = Blueprint('user_favorite_recipe', __name__)
user_favorite_recipe_schema = UserFavoriteRecipeSchema()
response_schema = ResponseSchema()
user_favorite_recipe_service = UserFavoriteRecipeService()

@user_favorite_recipe.route('/user_favorite_recipes', methods=['GET'])
def index():
    return {"user_favorite_recipes": user_favorite_recipe_schema.dump(user_favorite_recipe_service.all(), many=True)}, 200

@user_favorite_recipe.route('/user_favorite_recipes/<int:id>', methods=['GET'])
def find(id: int):
    response_builder = ResponseBuilder()
    user_favorite_recipe = user_favorite_recipe_service.find(id)
    if user_favorite_recipe:
        response_builder.add_message("Receta favorita encontrada").add_status_code(200).add_data(user_favorite_recipe_schema.dump(user_favorite_recipe))
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Receta favorita no encontrada").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404

@user_favorite_recipe.route('/user_favorite_recipes', methods=['POST'])
def create_user_favorite_recipe():
    user_favorite_recipe = user_favorite_recipe_schema.load(request.json)
    return {"user_favorite_recipe": user_favorite_recipe_schema.dump(user_favorite_recipe_service.save(user_favorite_recipe))}, 201

@user_favorite_recipe.route('/user_favorite_recipes/<int:id>', methods=['DELETE'])
def delete_user_favorite_recipe(id: int):
    user_favorite_recipe = user_favorite_recipe_service.find(id)
    if user_favorite_recipe:
        user_favorite_recipe_service.delete(user_favorite_recipe)
        response_builder = ResponseBuilder()
        response_builder.add_message("Receta favorita eliminada").add_status_code(200).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder = ResponseBuilder()
        response_builder.add_message("Receta favorita no encontrada").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404

@user_favorite_recipe.route('/user_favorite_recipes/user/<int:user_id>/recipe/<int:recipe_id>', methods=['GET'])
def find_by_user_and_recipe(user_id: int, recipe_id: int):
    user_favorite_recipe = user_favorite_recipe_service.find_by_user_and_recipe(user_id, recipe_id)
    if user_favorite_recipe:
        response_builder = ResponseBuilder()
        response_builder.add_message("Receta favorita encontrada").add_status_code(200).add_data(user_favorite_recipe_schema.dump(user_favorite_recipe))
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder = ResponseBuilder()
        response_builder.add_message("Receta favorita no encontrada").add_status_code(404).add_data({'user_id': user_id, 'recipe_id': recipe_id})
        return response_schema.dump(response_builder.build()), 404