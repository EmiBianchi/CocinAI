# Importar las dataclasses para crear clases con inicializadores automáticos
from dataclasses import dataclass
# Importar la tabla intermedia 'users_roles' que define la relación entre User y Role
from app.models.relations import users_roles
# Importar la instancia de la base de datos de la aplicación
from app import db

@dataclass(init=False, repr=True, eq=True)  # Decorador para crear una clase de datos sin inicializador automático
class Role(db.Model):  # Definición de la clase Role que hereda de db.Model
    __tablename__ = 'roles'  # Nombre de la tabla en la base de datos

    # Definición de los atributos de la tabla
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Clave primaria, se incrementa automáticamente
    name: str = db.Column(db.String(80), unique=True, nullable=False)  # Nombre del rol, debe ser único y no nulo
    description: str = db.Column(db.String(255), nullable=False)  # Descripción del rol, no puede ser nula

    # Relación Muchos a Muchos bidireccional con User
    # Permite que un rol tenga múltiples usuarios y que un usuario tenga múltiples roles
    users = db.relationship("User", secondary=users_roles, back_populates='roles')  
    
    # TODO: Implementar métodos para agregar, eliminar y listar usuarios en este rol
    def add_user(self, user):
        """
        Método para agregar un usuario a este rol.
        Si el usuario no está ya en la lista de usuarios, se agrega.
        """
        if user not in self.users:  # Verifica si el usuario ya está asociado al rol
            self.users.append(user)  # Agrega el usuario a la lista de usuarios asociados

    def remove_user(self, user):
        """
        Método para eliminar un usuario de este rol.
        Si el usuario está en la lista de usuarios, se elimina.
        """
        if user in self.users:  # Verifica si el usuario está asociado al rol
            self.users.remove(user)  # Elimina el usuario de la lista de usuarios asociados
