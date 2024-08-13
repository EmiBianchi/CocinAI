#class UserFavoriteRecipe(db.Model):
 #   __tablename__ = 'user_favorite_recipe'  # Nombre de la tabla en la base de datos

  #  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)  # Clave foránea a User
   # recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), primary_key=True)  # Clave foránea a Recipe

from app import db
from sqlalchemy.orm import relationship
from app.models import Recipe, User

recipe=Recipe()
user=User()

class RecipeFavorite(db.model):
    __tablename__="recipes_favorite"
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False) 

        # Relación hacia Recipe
    recipe = relationship('Recipe', backref="recipe_favorites", lazy=True)
    
    # Relación hacia User
    user = relationship('User', backref="recipe_favorites", lazy=True)
