from app import db
from sqlalchemy.orm import relationship

class Diet(db.Model):
    __tablename__ = 'diets'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)  # Clave primaria
    name = db.Column(db.String(50), nullable=False)  # Nombre de la dieta

    # Relaciones
    recipes = relationship('Recipe', secondary='recipe_diet', back_populates='diets')
    users = relationship('User', secondary='user_diet', back_populates='preferences')
