from app import db
from sqlalchemy.orm import relationship
from app.models import RecipeIngredient

class Recipe(db.Model):
    __tablename__ = 'recipes'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)  # Clave primaria
    title = db.Column(db.String(100), nullable=False)  # Título de la receta
    instructions = db.Column(db.Text, nullable=False)  # Instrucciones para la receta
    preparation_time = db.Column(db.Integer, nullable=False)  # Tiempo de preparación en minutos

    # Relaciones
    ingredients = relationship('Ingredient', secondary='recipe_ingredient', back_populates='recipes')
    recipe_favorites = relationship('RecipeFavorite', backref='recipe', lazy=True)
    recipe_ingredients = relationship('RecipeIngredient', backref='recipe', lazy=True)
    diets = relationship('Diet', secondary='recipe_diet', back_populates='recipes')
    favorited_by = relationship('User', secondary='user_favorite_recipe', back_populates='favorite_recipes')

    def __init__(self, title: str="default title", instructions: str="none", preparation_time: int=0):
        self.title = title
        self.instructions = instructions
        self.preparation_time = preparation_time

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "instructions": self.instructions,
            "preparation_time": self.preparation_time,
            "ingredients": [ingredient.to_json() for ingredient in self.recipe_ingredients],
            "diets": [diet.name for diet in self.diets],
        }

    def add_ingredient(self, ingredient, quantity):
        # Método para agregar un ingrediente a la receta
        recipe_ingredient = RecipeIngredient(recipe_id=self.id, ingredient_id=ingredient.id, quantity=quantity)
        db.session.add(recipe_ingredient)  # Agregar la relación a la sesión
        db.session.commit()  # Confirmar cambios en la base de datos

    def remove_ingredient(self, ingredient):
        # Método para eliminar un ingrediente de la receta
        recipe_ingredient = RecipeIngredient.query.filter_by(recipe_id=self.id, ingredient_id=ingredient.id).first()
        if recipe_ingredient:
            db.session.delete(recipe_ingredient)  # Eliminar la relación de la sesión
            db.session.commit()  # Confirmar cambios en la base de datos
