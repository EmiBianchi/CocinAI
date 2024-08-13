from typing import List
from app.models import Recipe
from app import db

class RecipeRepository:
    def save(self, recipe:Recipe)->Recipe:
        db.session.add(self, recipe)
        db.session.commit()
        return recipe
    
    def delate(self, recipe:Recipe)-> None:
        db.session.delete(recipe)
        db.session.commit()

    def find(self, id:int):
        return db.session.query(Recipe).filter(Recipe.id== id).one()
    
    def all(self) -> List["Recipe"]:
        recipes = db.session.query("Recipe").all()
        return recipes
    
    