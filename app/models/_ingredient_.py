from app import db
from sqlalchemy.orm import relationship

class Ingredient(db.Model):
    __tablename__ = 'ingredients'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)  # Clave primaria
    name = db.Column(db.String(50), nullable=False)  # Nombre del ingrediente
    unit_measurement = db.Column(db.String(20), nullable=False)  # Unidad de medida del ingrediente

    # Relaciones
    recipes = relationship('Recipe', secondary='recipe_ingredient', back_populates='ingredients')
