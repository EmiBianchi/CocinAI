from typing import List, Type
from app.models import User
from app import db
from app.models import UserData, Recipe

class UserRepository:
    """
    Aplicamos Responsabilidad Única y el Patrón Repository https://martinfowler.com/eaaCatalog/repository.html
    """
    def save(self, user: User) -> User:
        db.session.add(user) 
        db.session.commit()
        return user
    
    def update(self, user: User, id: int) -> User:
        entity = self.find(id)
        if entity is None:
            return None
        
        entity.username = user.username
        entity.email = user.email
        
        if user.password is not None:
            entity.password = user.password
        if user.data is not None:
            self.__update_data(entity, user.data)
 
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def delete(self, user: User) -> None:
        if user.data is not None:
            user.data.delete()
        user.delete()
        db.session.commit()
    
    def all(self) -> List[User]:
        users = db.session.query(User).all()
        return users
    
    def find(self, id: int) -> User:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(User).filter(User.id == id).one()
        except:
            return None
        
    def find_by_username(self, username: str):
        return db.session.query(User).filter(User.username == username).one_or_none()
    
    def find_by_email(self, email: str) -> User:
        #busqueda por like
        return db.session.query(User).filter(User.email == email).one_or_none()
    
    def search_recipes(self, ingredients):
        # Método para buscar recetas que contengan los ingredientes dados
        results = Recipe.query.filter(Recipe.ingredients.any(db.name.in_(ingredients))).all()
        # Filtrar recetas donde alguno de los ingredientes coincida con los dados y devolver todos los resultados
        return results

    def filter_recipes_diet(self, diet):
        # Método para filtrar recetas según la dieta preferida
        results = Recipe.query.filter(Recipe.diets.any(name=diet)).all()
        # Filtrar recetas que coincidan con la dieta dada y devolver todos los resultados
        return results
    
    def get_favorite_recipes(self, user: User) -> List[Recipe]:
        return user.favorite_recipes

    def add_favorite_recipe(self, user: User, recipe: Recipe) -> None:
        if recipe not in user.favorite_recipes:
            user.favorite_recipes.append(recipe)
            db.session.commit()

    def remove_favorite_recipe(self, user: User, recipe: Recipe) -> None:
        if recipe in user.favorite_recipes:
            user.favorite_recipes.remove(recipe)
            db.session.commit()

    def __update_data(self, entity: User, data: UserData):
        entity.data.firstname = data.firstname
        entity.data.lastname = data.lastname
        entity.data.phone = data.phone
        entity.data.address = data.address
        entity.data.city = data.city
        entity.data.country = data.country