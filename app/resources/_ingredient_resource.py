from flask import Blueprint, request
from app.mapping import IngredientSchema, ResponseSchema 
from app.services.response_message import ResponseBuilder
from app.services.ingredient_services import IngredientService

ingredient = Blueprint('ingredient', __name__)
ingredient_schema = IngredientSchema()
response_schema = ResponseSchema()
ingredient_service = IngredientService()

@ingredient.route('/ingredients', methods=['GET'])
def index():
    """
    Obtiene todos los ingredientes
    :return: JSON con la lista de todos los ingredientes
    """
    return {"ingredients": ingredient_schema.dump(ingredient_service.get_all(), many=True)}, 200

@ingredient.route('/ingredients/<int:id>', methods=['GET'])
def find(id: int):
    """
    Busca un ingrediente por su ID
    :param id: ID del ingrediente a buscar
    :return: JSON con los datos del ingrediente si se encuentra, o un mensaje de error si no
    """
    response_builder = ResponseBuilder()
    ingredient = ingredient_service.get_by_id(id)
    if ingredient:
        response_builder.add_message("Ingrediente encontrado").add_status_code(200).add_data(ingredient_schema.dump(ingredient))
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Ingrediente no encontrado").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404

@ingredient.route('/ingredients', methods=['POST'])
def create_ingredient():
    """
    Crea un nuevo ingrediente
    :return: JSON con los datos del ingrediente creado
    """
    data = request.json
    new_ingredient = ingredient_service.create(data['name'], data['unit_measurement'])
    return {"ingredient": ingredient_schema.dump(new_ingredient)}, 201

@ingredient.route('/ingredients/<int:id>', methods=['PUT'])
def update_ingredient(id: int):
    """
    Actualiza un ingrediente existente
    :param id: ID del ingrediente a actualizar
    :return: JSON con los datos del ingrediente actualizado, o un mensaje de error si no se encuentra
    """
    data = request.json
    ingredient = ingredient_service.get_by_id(id)
    if ingredient:
        updated_ingredient = ingredient_service.update(ingredient, data['name'], data['unit_measurement'])
        response_builder = ResponseBuilder()
        response_builder.add_message("Ingrediente actualizado").add_status_code(200).add_data(ingredient_schema.dump(updated_ingredient))
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder = ResponseBuilder()
        response_builder.add_message("Ingrediente no encontrado").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404

@ingredient.route('/ingredients/<int:id>', methods=['DELETE'])
def delete_ingredient(id: int):
    """
    Elimina un ingrediente
    :param id: ID del ingrediente a eliminar
    :return: JSON con un mensaje de éxito si se elimina, o un mensaje de error si no se encuentra
    """
    ingredient = ingredient_service.get_by_id(id)
    if ingredient:
        ingredient_service.delete(ingredient)
        response_builder = ResponseBuilder()
        response_builder.add_message("Ingrediente eliminado").add_status_code(200).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder = ResponseBuilder()
        response_builder.add_message("Ingrediente no encontrado").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404