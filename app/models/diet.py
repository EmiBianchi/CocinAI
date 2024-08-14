from app import db
from app.models import AuditMixin
from dataclasses import dataclass

@dataclass (init=False, repr=True, eq=True)

# Definición del modelo Diet
class Diet(db.Model, AuditMixin):
    __tablename__ = 'diets'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)  # Clave primaria de la dieta
    name = db.Column(db.String(50), nullable=False)  # Nombre de la dieta, no puede ser nulo

    # Definición de relaciones
    recipes = db.relationship('Recipe', secondary='recipe_diet', back_populates='diets')  # Relación muchos a muchos con recetas a través de la tabla intermedia 'recipe_diet'

    def __init__(self, name: str):
        # Método constructor para inicializar una dieta
        self.name = name  # Asignar el nombre de la dieta

    def to_json(self):
        # Método para convertir el objeto Diet a un diccionario JSON
        return {
            "id": self.id,  # ID de la dieta
            "name": self.name  # Nombre de la dieta
        }
