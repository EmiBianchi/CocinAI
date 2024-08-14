from typing import List, Type
from app.models import User
from app import db
from app.models import UserData, Recipe

class UserRepository:
    """
    Aplicamos Responsabilidad Única y el Patrón Repository
    https://martinfowler.com/eaaCatalog/repository.html
    """
    def save(self, user: User) -> User:
        """
        Guarda un usuario en la base de datos.
        
        :param user: Instancia del modelo User a guardar.
        :return: El usuario guardado.
        """
        db.session.add(user)  # Agrega el usuario a la sesión de la base de datos.
        db.session.commit()  # Confirma los cambios y guarda el usuario en la base de datos.
        return user  # Devuelve el usuario guardado.
    
    def update(self, user: User, id: int) -> User:
        """
        Actualiza un usuario existente en la base de datos.
        
        :param user: Instancia del modelo User con los nuevos datos.
        :param id: ID del usuario a actualizar.
        :return: El usuario actualizado o None si no se encontró.
        """
        entity = self.find(id)  # Busca el usuario existente por ID.
        if entity is None:
            return None  # Retorna None si no se encuentra el usuario.
        
        # Actualiza los atributos del usuario existente.
        entity.username = user.username
        entity.email = user.email
        
        if user.password is not None:
            entity.password = user.password
        if user.data is not None:
            self.__update_data(entity, user.data)  # Llama al método privado para actualizar los datos del usuario.

        db.session.add(entity)  # Agrega el usuario actualizado a la sesión.
        db.session.commit()  # Confirma los cambios en la base de datos.
        return entity  # Devuelve el usuario actualizado.
    
    def delete(self, user: User) -> None:
        """
        Elimina un usuario de la base de datos.
        
        :param user: Instancia del modelo User a eliminar.
        """
        if user.data is not None:
            user.data.delete()  # Elimina los datos asociados al usuario.
        db.session.delete(user)  # Elimina el usuario de la sesión.
        db.session.commit()  # Confirma los cambios y elimina el usuario de la base de datos.
    
    def all(self) -> List[User]:
        """
        Obtiene todos los usuarios de la base de datos.
        
        :return: Lista de todos los usuarios.
        """
        users = db.session.query(User).all()  # Consulta y devuelve todos los usuarios en la base de datos.
        return users
    
    def find(self, id: int) -> User:
        """
        Busca un usuario en la base de datos por su ID.
        
        :param id: ID del usuario a buscar.
        :return: El usuario encontrado o None si no se encuentra.
        """
        if id is None or id == 0:
            return None  # Retorna None si el ID es inválido.
        try:
            return db.session.query(User).filter(User.id == id).one()  # Devuelve el usuario con el ID especificado.
        except:
            return None  # Retorna None si no se encuentra el usuario.
        
    def find_by_username(self, username: str):
        """
        Busca un usuario por su nombre de usuario.
        
        :param username: Nombre de usuario a buscar.
        :return: El usuario encontrado o None si no se encuentra.
        """
        return db.session.query(User).filter(User.username == username).one_or_none()  # Retorna el usuario o None.

    def find_by_email(self, email: str) -> User:
        """
        Busca un usuario por su correo electrónico.
        
        :param email: Correo electrónico a buscar.
        :return: El usuario encontrado o None si no se encuentra.
        """
        return db.session.query(User).filter(User.email.like(email)).one_or_none()  # Retorna el usuario o None.
    
    def search_recipes(self, ingredients):
        """
        Busca recetas que contengan los ingredientes dados.
        
        :param ingredients: Lista de ingredientes a buscar.
        :return: Lista de recetas que contengan los ingredientes.
        """
        results = Recipe.query.filter(Recipe.ingredients.any(db.name.in_(ingredients))).all()
        # Filtra y devuelve las recetas que contengan alguno de los ingredientes dados.
        return results

    def filter_recipes_diet(self, diet):
        """
        Filtra recetas según la dieta preferida.
        
        :param diet: Tipo de dieta a filtrar.
        :return: Lista de recetas que coincidan con la dieta dada.
        """
        results = Recipe.query.filter(Recipe.diets.any(name=diet)).all()
        # Filtra y devuelve las recetas que coincidan con la dieta dada.
        return results
    
    def get_favorite_recipes(self, user: User) -> List[Recipe]:
        """
        Obtiene las recetas favoritas de un usuario.
        
        :param user: Instancia del modelo User.
        :return: Lista de recetas favoritas del usuario.
        """
        return user.favorite_recipes  # Devuelve las recetas favoritas del usuario.

    def add_favorite_recipe(self, user: User, recipe: Recipe) -> None:
        """
        Agrega una receta a las favoritas del usuario.
        
        :param user: Instancia del modelo User.
        :param recipe: Instancia del modelo Recipe a agregar a favoritos.
        """
        if recipe not in user.favorite_recipes:
            user.favorite_recipes.append(recipe)  # Agrega la receta a las favoritas del usuario.
            db.session.commit()  # Confirma los cambios en la base de datos.

    def remove_favorite_recipe(self, user: User, recipe: Recipe) -> None:
        """
        Elimina una receta de las favoritas del usuario.
        
        :param user: Instancia del modelo User.
        :param recipe: Instancia del modelo Recipe a eliminar de favoritos.
        """
        if recipe in user.favorite_recipes:
            user.favorite_recipes.remove(recipe)  # Elimina la receta de las favoritas del usuario.
            db.session.commit()  # Confirma los cambios en la base de datos.

    def __update_data(self, entity: User, data: UserData):
        """
        Método privado para actualizar los datos personales del usuario.
        
        :param entity: Instancia del modelo User a actualizar.
        :param data: Instancia del modelo UserData con los nuevos datos.
        """
        entity.data.firstname = data.firstname
        entity.data.lastname = data.lastname
        entity.data.phone = data.phone
        entity.data.address = data.address
        entity.data.city = data.city
        entity.data.country = data.country
