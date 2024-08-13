from dataclasses import dataclass  # Importar el decorador dataclass para crear clases de datos
from app import db  # Importar la instancia de la base de datos de la aplicación
from app.models.audit_mixin import AuditMixin  # Importar el mixin de auditoría
from app.models.soft_delete import SoftDeleteMixin  # Importar el mixin para eliminación suave

# Definición de la clase Profile que hereda de SoftDeleteMixin, AuditMixin y db.Model
@dataclass(init=False, repr=True, eq=True)  # Decorador que permite crear automáticamente métodos de inicialización, representación y comparación
class Profile(SoftDeleteMixin, AuditMixin, db.Model):
    __tablename__ = 'profiles'  # Nombre de la tabla en la base de datos

    # Definición de los atributos de la clase como columnas de la base de datos
    id: int = db.Column(db.Integer, primary_key=True)  # Clave primaria, tipo de dato entero
    name: str = db.Column(db.String(50), nullable=False)  # Nombre del perfil, tipo de dato cadena, no puede ser nulo

    # Definición de relaciones
    data = db.relationship('UserData', back_populates='profile')  # Relación Uno a Muchos bidireccional con UserData, permite acceder a los datos de usuario asociados
