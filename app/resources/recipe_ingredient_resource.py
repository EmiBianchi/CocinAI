from flask import Blueprint, request
from app.mapping import RecipeIngredientSchema, ResponseSchema
from app.services.response_message import ResponseBuilder
from app.services.recipe_ingredient_services import RecipeIngredientService

recipe_ingredient = Blueprint('recipe_ingredient', __name__)
recipe_ingredient_schema = RecipeIngredientSchema()
response_schema = ResponseSchema()
recipe_ingredient_service = RecipeIngredientService()

@recipe_ingredient.route('/recipe_ingredients', methods=['POST'])
def create_recipe_ingredient():
    """
    Crea una nueva relación entre receta e ingrediente
    :return: JSON con los datos de la relación creada
    """
    data = request.json
    new_recipe_ingredient = recipe_ingredient_service.create(data['recipe_id'], data['ingredient_id'], data['quantity'])
    return {"recipe_ingredient": recipe_ingredient_schema.dump(new_recipe_ingredient)}, 201

@recipe_ingredient.route('/recipe_ingredients/<int:recipe_id>/<int:ingredient_id>', methods=['GET'])
def get_recipe_ingredient(recipe_id: int, ingredient_id: int):
    """
    Obtiene una relación específica entre receta e ingrediente
    :param recipe_id: ID de la receta
    :param ingredient_id: ID del ingrediente
    :return: JSON con los datos de la relación si se encuentra, o un mensaje de error si no
    """
    recipe_ingredient = recipe_ingredient_service.get_by_ids(recipe_id, ingredient_id)
    if recipe_ingredient:
        response_builder = ResponseBuilder()
        response_builder.add_message("Ingrediente de receta encontrado").add_status_code(200).add_data(recipe_ingredient_schema.dump(recipe_ingredient))
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder = ResponseBuilder()
        response_builder.add_message("Ingrediente de receta no encontrado").add_status_code(404).add_data({'recipe_id': recipe_id, 'ingredient_id': ingredient_id})
        return response_schema.dump(response_builder.build()), 404

@recipe_ingredient.route('/recipe_ingredients/<int:recipe_id>/<int:ingredient_id>', methods=['PUT'])
def update_recipe_ingredient(recipe_id: int, ingredient_id: int):
    """
    Actualiza una relación existente entre receta e ingrediente
    :param recipe_id: ID de la receta
    :param ingredient_id: ID del ingrediente
    :return: JSON con los datos de la relación actualizada, o un mensaje de error si no se encuentra
    """
    data = request.json
    recipe_ingredient = recipe_ingredient_service.get_by_ids(recipe_id, ingredient_id)
    if recipe_ingredient:
        updated_recipe_ingredient = recipe_ingredient_service.update(recipe_ingredient, data['quantity'])
        response_builder = ResponseBuilder()
        response_builder.add_message("Ingrediente de receta actualizado").add_status_code(200).add_data(recipe_ingredient_schema.dump(updated_recipe_ingredient))
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder = ResponseBuilder()
        response_builder.add_message("Ingrediente de receta no encontrado").add_status_code(404).add_data({'recipe_id': recipe_id, 'ingredient_id': ingredient_id})
        return response_schema.dump(response_builder.build()), 404

@recipe_ingredient.route('/recipe_ingredients/<int:recipe_id>/<int:ingredient_id>', methods=['DELETE'])
def delete_recipe_ingredient(recipe_id: int, ingredient_id: int):
    """
    Elimina una relación entre receta e ingrediente
    :param recipe_id: ID de la receta
    :param ingredient_id: ID del ingrediente
    :return: JSON con un mensaje de éxito si se elimina, o un mensaje de error si no se encuentra
    """
    recipe_ingredient = recipe_ingredient_service.get_by_ids(recipe_id, ingredient_id)
    if recipe_ingredient:
        recipe_ingredient_service.delete(recipe_ingredient)
        response_builder = ResponseBuilder()
        response_builder.add_message("Ingrediente de receta eliminado").add_status_code(200).add_data({'recipe_id': recipe_id, 'ingredient_id': ingredient_id})
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder = ResponseBuilder()
        response_builder.add_message("Ingrediente de receta no encontrado").add_status_code(404).add_data({'recipe_id': recipe_id, 'ingredient_id': ingredient_id})
        return response_schema.dump(response_builder.build()), 404
