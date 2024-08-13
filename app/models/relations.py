from app import db # Importar la instancia de la base de datos de la aplicación

"""
Relación Muchos a Muchos bidireccional entre User y Role.
Esta relación permite que un usuario pueda tener múltiples roles y que un rol pueda ser asignado a múltiples usuarios.
Se crea una tabla intermedia llamada users_roles que almacena las asociaciones entre usuarios y roles.
"""
# Definición de la tabla intermedia 'users_roles'
users_roles = db.Table(
    'users_roles',  # Nombre de la tabla en la base de datos
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),  # Columna user_id que hace referencia a la tabla 'users' como clave foránea
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True)  # Columna role_id que hace referencia a la tabla 'roles' como clave foránea
)
