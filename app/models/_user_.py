from app import db
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)  # Clave primaria
    name = db.Column(db.String(50), nullable=False)  # Nombre del usuario
    email = db.Column(db.String(120), unique=True, nullable=False)  # Correo electrónico único
    password = db.Column(db.String(128), nullable=False)  # Contraseña del usuario (debería estar hasheada)

    # Relaciones
    favorite_recipes = relationship('Recipe', secondary='user_favorite_recipe', back_populates='favorited_by')
    preferences = relationship('Diet', secondary='user_diet', back_populates='users')

    def search_recipes(self, ingredients):
        # Método para buscar recetas que contengan los ingredientes dados
        from app.models.recipe import Recipe  # Importar el modelo Recipe
        results = Recipe.query.filter(Recipe.ingredients.any(name.in_(ingredients))).all()
        return results

    def filter_recipes_diet(self, diet):
        # Método para filtrar recetas según la dieta preferida
        from app.models.recipe import Recipe  # Importar el modelo Recipe
        results = Recipe.query.filter(Recipe.diets.any(name=diet)).all()
        return results

    def save_favorite_recipe(self, recipe):
        # Método para guardar una receta como favorita
        if recipe not in self.favorite_recipes:
            self.favorite_recipes.append(recipe)  # Agregar la receta a las favoritas
            db.session.commit()  # Confirmar cambios en la base de datos

    def remove_favorite_recipe(self, recipe):
        # Método para eliminar una receta de favoritos
        if recipe in self.favorite_recipes:
            self.favorite_recipes.remove(recipe)  # Remover la receta de las favoritas
            db.session.commit()  # Confirmar cambios en la base de datos
