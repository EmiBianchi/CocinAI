from app import db
from app.models import AuditMixin
from dataclasses import dataclass

@dataclass (init=False, repr=True, eq=True)

# Definición del modelo Ingredient que representa un ingrediente en la base de datos
class Ingredient(db.Model, AuditMixin):
    __tablename__ = 'ingredients'  # Nombre de la tabla en la base de datos

    # Definición de las columnas del modelo
    id = db.Column(db.Integer, primary_key=True)  # Clave primaria del ingrediente, que identifica de manera única a cada registro
    name = db.Column(db.String(50), nullable=False)  # Nombre del ingrediente, debe ser una cadena de hasta 50 caracteres y no puede ser nulo
    unit_measurement = db.Column(db.String(20), nullable=False)  # Unidad de medida del ingrediente, debe ser una cadena de hasta 20 caracteres y no puede ser nulo

    # Relaciones entre el modelo Ingredient y otros modelos
    recipes = db.relationship('Recipe', secondary='recipe_ingredient', back_populates='ingredients')
    # Define una relación muchos a muchos con el modelo Recipe a través de la tabla intermedia 'recipe_ingredient'.
    # Esto permite asociar múltiples recetas con múltiples ingredientes.

    def to_json(self):
        # Método para convertir el objeto Ingredient a un diccionario JSON
        return {
            "id": self.id,  # ID del ingrediente
            "name": self.name,  # Nombre del ingrediente
            "unit_measurement": self.unit_measurement,  # Unidad de medida del ingrediente
        }
