from app import db
from sqlalchemy.orm import relationship

class RecipeFavorite(db.Model):  # La "M" en "Model" debe estar en mayúscula
    __tablename__ = "recipes_favorite"
    
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Clave foránea a User
    
    # Relación hacia Recipe
    recipe = relationship('Recipe', backref="recipe_favorites", lazy=True)
    
    # Relación hacia User
    user = relationship('User', backref="recipe_favorites", lazy=True)
