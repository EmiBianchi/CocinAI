from app import db
from app.models import RecipeIngredient, AuditMixin
from dataclasses import dataclass

@dataclass (init=False, repr=True, eq=True)

# Definición del modelo Recipe
class Recipe(db.Model, AuditMixin):
    __tablename__ = 'recipes'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)  # Clave primaria de la receta
    title = db.Column(db.String(100), nullable=False)  # Título de la receta, no puede ser nulo
    instructions = db.Column(db.Text, nullable=False)  # Instrucciones para preparar la receta, no puede ser nulo
    preparation_time = db.Column(db.Integer, nullable=False)  # Tiempo de preparación en minutos, no puede ser nulo

    # Definición de relaciones
    ingredients = db.relationship('Ingredient', secondary='recipe_ingredient', back_populates='recipes')  # Relación Muchos a Muchos con ingredientes a través de la tabla intermedia 'recipe_ingredient'
    diets = db.relationship('Diet', secondary='recipe_diet', back_populates='recipes')  # Relación Muchos a Muchos con dietas
    user_favorite_recipe = db.relationship('UserFavoriteRecipe', backref='recipe', lazy=True)  # Relación con recetas favoritas del usuario
    recipe_ingredients = db.relationship('RecipeIngredient', backref='recipe', lazy=True)  # Relación Uno a Muchos con la tabla intermedia 'RecipeIngredient'

    def __init__(self, title: str = "default title", instructions: str = "none", preparation_time: int = 0):
        # Método constructor para inicializar una receta
        self.title = title  # Asignar el título de la receta
        self.instructions = instructions  # Asignar las instrucciones de la receta
        self.preparation_time = preparation_time  # Asignar el tiempo de preparación de la receta

    def to_json(self):
        # Método para convertir el objeto Recipe a un diccionario JSON
        return {
            "id": self.id,  # ID de la receta
            "title": self.title,  # Título de la receta
            "instructions": self.instructions,  # Instrucciones de la receta
            "preparation_time": self.preparation_time,  # Tiempo de preparación de la receta
            "ingredients": [ingredient.to_json() for ingredient in self.recipe_ingredients],  # Lista de ingredientes en formato JSON
            "diets": [diet.name for diet in self.diets],  # Lista de nombres de dietas asociadas a la receta
        }

    def add_ingredient(self, ingredient, quantity):
        # Método para agregar un ingrediente a la receta
        recipe_ingredient = RecipeIngredient(recipe_id=self.id, ingredient_id=ingredient.id, quantity=quantity)  # Crear una nueva relación RecipeIngredient
        db.session.add(recipe_ingredient)  # Agregar la relación a la sesión
        db.session.commit()  # Confirmar cambios en la base de datos

    def remove_ingredient(self, ingredient):
        # Método para eliminar un ingrediente de la receta
        recipe_ingredient = RecipeIngredient.query.filter_by(recipe_id=self.id, ingredient_id=ingredient.id).first()  # Buscar la relación RecipeIngredient
        if recipe_ingredient:
            db.session.delete(recipe_ingredient)  # Eliminar la relación de la sesión
            db.session.commit()  # Confirmar cambios en la base de datos
