from datetime import datetime as dt  # Importar la clase datetime para manejar fechas y horas
from sqlalchemy import Column, Integer, DateTime, ForeignKey  # Importar tipos de columnas y claves foráneas
from sqlalchemy.ext.declarative import declared_attr  # Importar declared_attr para definir atributos en clases
from sqlalchemy.orm import relationship  # Importar relationship para establecer relaciones entre modelos

# Definición de la clase AuditMixin que proporciona columnas de auditoría
class AuditMixin(object):
    """
    Mixin para columnas de auditoría.
    Este mixin agrega automáticamente columnas de auditoría a los modelos que lo heredan.
    Documentación: https://docs.sqlalchemy.org/en/20/orm/declarative_mixins.html#mixing-in-columns
    """

    @declared_attr  # Decorador que indica que el atributo es declarado y se define en la subclase
    def created_by_id(cls):
        # Definición de la columna 'created_by_id' que almacena el ID del usuario que creó el registro
        return Column(
            Integer,  # Tipo de dato entero
            ForeignKey('users.id', name='fk_%s_created_by_id' % cls.__name__, use_alter=True),  # Clave foránea hacia la tabla 'users'
            nullable=True  # Permitir valores nulos
        )
    
    @declared_attr  # Decorador para definir la relación en la subclase
    def created_by(cls):
        # Relación que establece el vínculo con el modelo 'User' utilizando el 'created_by_id'
        return relationship('User', primaryjoin='User.id == %s.created_by_id' % cls.__name__, remote_side='User.id')
    
    @declared_attr  # Decorador para definir el atributo
    def updated_by_id(cls):
        # Definición de la columna 'updated_by_id' que almacena el ID del usuario que actualizó el registro
        return Column(
            Integer,  # Tipo de dato entero
            ForeignKey('users.id', name='fk_%s_updated_by_id' % cls.__name__, use_alter=True),  # Clave foránea hacia la tabla 'users'
            nullable=True  # Permitir valores nulos
        )

    @declared_attr  # Decorador para definir la relación en la subclase
    def updated_by(cls):
        # Relación que establece el vínculo con el modelo 'User' utilizando el 'updated_by_id'
        return relationship('User', primaryjoin='User.id == %s.updated_by_id' % cls.__name__, remote_side='User.id')
    
    # Definición de columnas de auditoría para rastrear cuándo se creó y se actualizó un registro
    created_at = Column(DateTime, nullable=False, default=dt.now())  # Columna que almacena la fecha de creación, no puede ser nula
    updated_at = Column(DateTime, nullable=False, default=dt.now(), onupdate=dt.now())  # Columna que almacena la fecha de actualización, se actualiza automáticamente
