from typing import List
from app.models import UserFavoriteRecipe
from app import db

class UserFavoriteRecipeRepository:
    def save(self, user_favorite_recipe: UserFavoriteRecipe) -> UserFavoriteRecipe:
        db.session.add(user_favorite_recipe)  # Añade el objeto a la sesión de la base de datos.
        db.session.commit()  # Realiza la operación de guardado en la base de datos.
        return user_favorite_recipe  # Retorna el objeto guardado.
    
    def delete(self, user_favorite_recipe: UserFavoriteRecipe) -> None:
        db.session.delete(user_favorite_recipe)  # Elimina el objeto de la sesión de la base de datos.
        db.session.commit()  # Realiza la operación de eliminación en la base de datos.

    def find(self, id: int) -> UserFavoriteRecipe:
        return db.session.query(UserFavoriteRecipe).filter(UserFavoriteRecipe.id == id).one_or_none()
        # Realiza una consulta en la base de datos para buscar un UserFavoriteRecipe por su ID.
        # Retorna el objeto encontrado o None si no se encuentra ningún resultado.
    
    def find_by_user_and_recipe(self, user_id: int, recipe_id: int) -> UserFavoriteRecipe:
        return db.session.query(UserFavoriteRecipe).filter(
            UserFavoriteRecipe.user_id == user_id,  # Filtra por el ID del usuario.
            UserFavoriteRecipe.recipe_id == recipe_id  # Filtra por el ID de la receta.
        ).one_or_none()
        # Realiza una consulta en la base de datos para buscar una relación UserFavoriteRecipe
        # que coincida con el ID del usuario y el ID de la receta. Retorna el objeto encontrado
        # o None si no se encuentra ningún resultado.

    def all(self) -> List[UserFavoriteRecipe]:
        return db.session.query(UserFavoriteRecipe).all()
        # Realiza una consulta para obtener todas las relaciones UserFavoriteRecipe almacenadas en la base de datos.
