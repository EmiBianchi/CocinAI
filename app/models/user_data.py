# Importar el decorador dataclass para simplificar la definición de clases
from dataclasses import dataclass
# Importar la instancia de la base de datos de la aplicación
from app import db
# Importar el mixin para auditoría
from app.models.audit_mixin import AuditMixin
# Importar el mixin para eliminación suave
from app.models.soft_delete import SoftDeleteMixin

@dataclass(init=False, repr=True, eq=True)  # Decorador para generar métodos especiales automáticamente
class UserData(SoftDeleteMixin, db.Model):  # Clase UserData que hereda de SoftDeleteMixin y db.Model
    __tablename__ = 'users_data'  # Nombre de la tabla en la base de datos

    # Definición de los campos de la tabla
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Clave primaria que se autoincrementa
    firstname: str = db.Column(db.String(80), nullable=False)  # Nombre del usuario, no puede ser nulo
    lastname: str = db.Column(db.String(80), nullable=False)  # Apellido del usuario, no puede ser nulo
    phone: str = db.Column(db.String(120), nullable=False)  # Número de teléfono del usuario, no puede ser nulo
    address: str = db.Column(db.String(120), nullable=False)  # Dirección del usuario, no puede ser nulo
    city: str = db.Column(db.String(120), nullable=False)  # Ciudad del usuario, no puede ser nulo
    country: str = db.Column(db.String(120), nullable=False)  # País del usuario, no puede ser nulo

    # Clave foránea para la relación con la tabla 'users'
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))  
    # Relación Uno a Uno bidireccional con User
    # Establece una relación con la clase User, donde 'data' es la propiedad en User
    user = db.relationship("User", back_populates='data', uselist=False)  # Relación Uno a Uno, no se permite una lista

    # Clave foránea para la relación con la tabla 'profiles'
    profile_id = db.Column('profile_id', db.Integer, db.ForeignKey('profiles.id'))  
    # Relación Muchos a Uno bidireccional con Profile
    profile = db.relationship("Profile", back_populates='data')  # Establece una relación con la clase Profile

    def __init__(self, firstname: str = None, lastname: str = None, phone: str = None, address: str = None, city: str = None, country: str = None, profile = None):
        # Constructor para inicializar los atributos de la clase
        self.firstname = firstname  # Asignar el nombre
        self.lastname = lastname  # Asignar el apellido
        self.phone = phone  # Asignar el número de teléfono
        self.address = address  # Asignar la dirección
        self.city = city  # Asignar la ciudad
        self.country = country  # Asignar el país
        self.profile = profile  # Asignar el perfil (si se proporciona)
