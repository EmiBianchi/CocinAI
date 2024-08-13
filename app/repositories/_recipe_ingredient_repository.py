from app import db
from app.models import RecipeIngredient

class RecipeIngredientRepository:
    def create(recipe_id: int, ingredient_id: int, quantity: float) -> RecipeIngredient:
        recipe_ingredient = RecipeIngredient(recipe_id=recipe_id, ingredient_id=ingredient_id, quantity=quantity)
        # Crea una nueva instancia de RecipeIngredient con los IDs de receta e ingrediente, y la cantidad.

        db.session.add(recipe_ingredient)  # Añade la nueva relación a la sesión de la base de datos.
        db.session.commit()  # Guarda los cambios en la base de datos.
        return recipe_ingredient  # Retorna la instancia creada de RecipeIngredient.

    def get_by_ids(recipe_id: int, ingredient_id: int) -> RecipeIngredient:
        return RecipeIngredient.query.filter_by(recipe_id=recipe_id, ingredient_id=ingredient_id).first()
        # Realiza una consulta para buscar una relación RecipeIngredient por los IDs de receta e ingrediente.
        # Retorna la instancia encontrada o None si no se encuentra.

    def update(recipe_ingredient: RecipeIngredient, quantity: float) -> RecipeIngredient:
        recipe_ingredient.quantity = quantity  # Actualiza la cantidad del ingrediente en la receta.
        db.session.commit()  # Guarda los cambios en la base de datos.
        return recipe_ingredient  # Retorna la instancia actualizada de RecipeIngredient.

    def delete(recipe_ingredient: RecipeIngredient) -> None:
        db.session.delete(recipe_ingredient)  # Elimina la relación de la sesión de la base de datos.
        db.session.commit()  # Guarda los cambios en la base de datos.
