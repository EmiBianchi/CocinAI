from app import db
from sqlalchemy.orm import relationship

class RecipeIngredient(db.Model):
    __tablename__ = 'recipe_ingredient'  # Nombre de la tabla en la base de datos

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), primary_key=True)  # Clave foránea a Recipe
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'), primary_key=True)  # Clave foránea a Ingredient
    quantity = db.Column(db.Float, nullable=False)  # Cantidad del ingrediente
    
    # Relación hacia Recipe
    recipe = relationship('Recipe', backref="recipe_ingredients", lazy=True)
    
    # Relación hacia Ingredient
    ingredient = relationship('Ingredient', backref="recipe_ingredients", lazy=True)
