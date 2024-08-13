from app import db
from app.models import Ingredient

from app import db
from app.models import Ingredient

class IngredientRepository:
    def create(name: str, unit_measurement: str) -> Ingredient:
        ingredient = Ingredient(name=name, unit_measurement=unit_measurement)
        # Crea una nueva instancia de Ingredient con el nombre y la unidad de medida proporcionados.
        db.session.add(ingredient)  # Añade el nuevo ingrediente a la sesión de la base de datos.
        db.session.commit()  # Guarda los cambios en la base de datos.
        return ingredient  # Retorna el ingrediente creado.

    def get_by_id(ingredient_id: int) -> Ingredient:
       return Ingredient.query.get(ingredient_id) # Realiza una consulta para obtener un ingrediente por su ID. Retorna la instancia encontrada o None si no se encuentra.

    def get_all() -> list[Ingredient]:
       return Ingredient.query.all()
        # Realiza una consulta para obtener todos los ingredientes almacenados en la base de datos.
        # Retorna una lista con todas las instancias de Ingredient.

    def update(ingredient: Ingredient, name: str, unit_measurement: str) -> Ingredient:
        ingredient.name = name  # Actualiza el nombre del ingrediente.
        ingredient.unit_measurement = unit_measurement  # Actualiza la unidad de medida del ingrediente.
        db.session.commit()  # Guarda los cambios en la base de datos.
        return ingredient  # Retorna la instancia actualizada del ingrediente.

    def delete(ingredient: Ingredient) -> None:
        db.session.delete(ingredient)  # Elimina el ingrediente de la sesión de la base de datos.
        db.session.commit()  # Guarda los cambios en la base de datos.

    