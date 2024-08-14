from flask import Blueprint, request
from app.mapping import RecipeSchema, ResponseSchema
from app.services.response_message import ResponseBuilder
from app.services.recipe_services import RecipeService

recipe = Blueprint('recipe', __name__)
recipe_schema = RecipeSchema()
response_schema = ResponseSchema()
recipe_service = RecipeService()

@recipe.route('/recipes', methods=['GET'])
def index():
    """
    Obtiene todas las recetas
    :return: JSON con la lista de todas las recetas
    """
    return {"recipes": recipe_schema.dump(recipe_service.all(), many=True)}, 200

@recipe.route('/recipes/<int:id>', methods=['GET'])
def find(id: int):
    """
    Busca una receta por su ID
    :param id: ID de la receta a buscar
    :return: JSON con los datos de la receta si se encuentra, o un mensaje de error si no
    """
    response_builder = ResponseBuilder()
    recipe = recipe_service.find(id)
    if recipe:
        response_builder.add_message("Receta encontrada").add_status_code(200).add_data(recipe_schema.dump(recipe))
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Receta no encontrada").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404

@recipe.route('/recipes', methods=['POST'])
def create_recipe():
    """
    Crea una nueva receta
    :return: JSON con los datos de la receta creada
    """
    recipe = recipe_schema.load(request.json)
    return {"recipe": recipe_schema.dump(recipe_service.save(recipe))}, 201

@recipe.route('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id: int):
    """
    Actualiza una receta existente
    :param id: ID de la receta a actualizar
    :return: JSON con los datos de la receta actualizada, o un mensaje de error si no se encuentra
    """
    recipe_data = recipe_schema.load(request.json)
    recipe = recipe_service.find(id)
    if recipe:
        updated_recipe = recipe_service.update(recipe, recipe_data)
        response_builder = ResponseBuilder()
        response_builder.add_message("Receta actualizada").add_status_code(200).add_data(recipe_schema.dump(updated_recipe))
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder = ResponseBuilder()
        response_builder.add_message("Receta no encontrada").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404

@recipe.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id: int):
    """
    Elimina una receta
    :param id: ID de la receta a eliminar
    :return: JSON con un mensaje de éxito si se elimina, o un mensaje de error si no se encuentra
    """
    recipe = recipe_service.find(id)
    if recipe:
        recipe_service.delete(recipe)
        response_builder = ResponseBuilder()
        response_builder.add_message("Receta eliminada").add_status_code(200).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder = ResponseBuilder()
        response_builder.add_message("Receta no encontrada").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404
