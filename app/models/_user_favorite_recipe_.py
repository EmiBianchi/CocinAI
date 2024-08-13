class UserFavoriteRecipe(db.Model):
    __tablename__ = 'user_favorite_recipe'  # Nombre de la tabla en la base de datos

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)  # Clave foránea a User
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), primary_key=True)  # Clave foránea a Recipe
