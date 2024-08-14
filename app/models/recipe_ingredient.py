from app import db
from dataclasses import dataclass

@dataclass (init=False, repr=True, eq=True)

class RecipeIngredient(db.Model):
    __tablename__ = 'recipe_ingredient'  # Nombre de la tabla en la base de datos

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), primary_key=True)  # Clave foránea a Recipe
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)  # Clave foránea a Ingredient
    quantity = db.Column(db.Float, nullable=False)  # Cantidad del ingrediente

    # Relaciones
    recipe = db.relationship('Recipe', backref="recipe_ingredients", lazy=True)
    ingredient = db.relationship('Ingredient', backref="recipe_ingredients", lazy=True)
