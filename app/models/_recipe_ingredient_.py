class RecipeIngredient(db.Model):
    __tablename__ = 'recipe_ingredient'  # Nombre de la tabla en la base de datos

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), primary_key=True)  # Clave foránea a Recipe
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'), primary_key=True)  # Clave foránea a Ingredient
    quantity = db.Column(db.Float, nullable=False)  # Cantidad del ingrediente
