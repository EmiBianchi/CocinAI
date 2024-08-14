from typing import List
from app.models import Recipe, RecipeIngredient
from app import db

class RecipeRepository:
    """
    Clase repositorio para manejar operaciones CRUD en el modelo Recipe.
    """

    def save(self, recipe: Recipe) -> Recipe:
        """
        Guarda una receta en la base de datos.
        
        :param recipe: Instancia del modelo Recipe a guardar.
        :return: La receta guardada.
        """
        db.session.add(recipe)  # Agrega la receta a la sesión de la base de datos.
        db.session.commit()  # Confirma los cambios y guarda la receta en la base de datos.
        return recipe  # Devuelve la receta guardada.
    
    def delete(self, recipe: Recipe) -> None:
        """
        Elimina una receta de la base de datos.
        
        :param recipe: Instancia del modelo Recipe a eliminar.
        """
        db.session.delete(recipe)  # Marca la receta para eliminación.
        db.session.commit()  # Confirma los cambios y elimina la receta de la base de datos.

    def find(self, id: int) -> Recipe:
        """
        Busca una receta en la base de datos por su ID.
        
        :param id: ID de la receta a buscar.
        :return: La receta encontrada.
        """
        return db.session.query(Recipe).filter(Recipe.id == id).one()  # Devuelve la receta con el ID especificado.
    
    def all(self) -> List["Recipe"]:
        """
        Obtiene todas las recetas de la base de datos.
        
        :return: Lista de todas las recetas.
        """
        recipes = db.session.query(Recipe).all()  # Consulta y devuelve todas las recetas en la base de datos.
        return recipes
