from app import db
from app.models import Recipe, Ingredient, RecipeIngredient

class RecipeRepository:
    def create(title: str, instructions: str, preparation_time: int) -> Recipe:
        recipe = Recipe(title=title, instructions=instructions, preparation_time=preparation_time)
        # Crea una nueva instancia de Recipe con el título, las instrucciones y el tiempo de preparación proporcionados.

        db.session.add(recipe)  # Añade la nueva receta a la sesión de la base de datos.
        db.session.commit()  # Guarda los cambios en la base de datos.
        return recipe  # Retorna la receta creada.

    def get_by_id(recipe_id: int) -> Recipe:
        return Recipe.query.get(recipe_id)
        # Realiza una consulta para obtener una receta por su ID. Retorna la instancia encontrada o None si no se encuentra.

    def get_all() -> list[Recipe]:
        return Recipe.query.all()
        # Realiza una consulta para obtener todas las recetas almacenadas en la base de datos.
        # Retorna una lista con todas las instancias de Recipe.

    def update(recipe: Recipe, title: str, instructions: str, preparation_time: int) -> Recipe:
        recipe.title = title  # Actualiza el título de la receta.
        recipe.instructions = instructions  # Actualiza las instrucciones de la receta.
        recipe.preparation_time = preparation_time  # Actualiza el tiempo de preparación de la receta.
        db.session.commit()  # Guarda los cambios en la base de datos.
        return recipe  # Retorna la instancia actualizada de la receta.

    def delete(recipe: Recipe) -> None:
        db.session.delete(recipe)  # Elimina la receta de la sesión de
