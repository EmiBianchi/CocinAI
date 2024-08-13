from app import db

class UserFavoriteRecipe(db.Model):
    __tablename__ = 'user_favorite_recipe'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)  # Clave foránea a Recipe
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Clave foránea a User
    
    # Relaciones
    recipe = db.relationship('Recipe', backref="recipe_favorites", lazy=True)
    user = db.relationship('User', backref="recipe_favorites", lazy=True)
