from app.models import Recipe, UserData, AuditMixin
from app import db
from app.models.relations import users_roles

# Definición del modelo User que representa un usuario en la base de datos
class User(db.Model, AuditMixin):
    __tablename__ = 'users'  # Nombre de la tabla en la base de datos

    # Definición de las columnas del modelo
    id = db.Column(db.Integer, primary_key=True)  # Clave primaria del usuario
    name = db.Column(db.String(50), nullable=False)  # Nombre del usuario, no puede ser nulo
    email = db.Column(db.String(120), unique=True, nullable=False)  # Correo electrónico del usuario, debe ser único y no puede ser nulo
    password = db.Column(db.String(128), nullable=False)  # Contraseña del usuario, debe estar hasheada y no puede ser nulo

    # Relaciones entre el modelo User y otros modelos
    data = db.relationship('UserData', uselist=False, back_populates='user')
    # Relación uno a uno con el modelo UserData (solo un conjunto de datos por usuario)
    roles = db.relationship("Role", secondary=users_roles, back_populates='users')
    # Relación muchos a muchos con el modelo Role a través de la tabla intermedia users_roles
    favorite_recipes = db.relationship('Recipe', secondary='user_favorite_recipe', back_populates='favorited_by')
    # Relación muchos a muchos con el modelo Recipe a través de la tabla intermedia user_favorite_recipe

    def __init__(self, name: str = None, password: str = None, email: str = None, data: UserData = None, favorite_recipes: str = None):
        # Constructor para inicializar los atributos del usuario
        self.data = data
        self.name = name
        self.password = password
        self.email = email
        self.favorite_recipes = favorite_recipes

    def to_json(self):
        # Método para convertir el objeto User a un diccionario JSON
        return {
            "id": self.id,  # ID del usuario
            "name": self.name,  # Nombre del usuario
            "email": self.email,  # Correo electrónico del usuario
            "favorite_recipes": [recipe.to_json() for recipe in self.favorite_recipes],
            # Lista de recetas favoritas convertidas a formato JSON (asumiendo que Recipe tiene un método to_json)
            "data": self.data.to_json() if self.data else None
            # Datos del usuario convertidos a formato JSON (asumiendo que UserData tiene un método to_json)
        }

    def add_role(self, role):
        # Método para agregar un rol al usuario
        if role not in self.roles:  # Comprobar si el rol ya no está asociado al usuario
            self.roles.append(role)  # Agregar el rol a la lista de roles del usuario

    def remove_role(self, role):
        # Método para eliminar un rol del usuario
        if role in self.roles:  # Comprobar si el rol está asociado al usuario
            self.roles.remove(role)  # Remover el rol de la lista de roles del usuario

    def save_favorite_recipe(self, recipe):
        # Método para guardar una receta como favorita
        if recipe not in self.favorite_recipes:  # Comprobar si la receta no está ya en favoritas
            self.favorite_recipes.append(recipe)  # Agregar la receta a las favoritas
            db.session.commit()  # Confirmar cambios en la base de datos

    def remove_favorite_recipe(self, recipe):
        # Método para eliminar una receta de favoritos
        if recipe in self.favorite_recipes:  # Comprobar si la receta está en favoritas
            self.favorite_recipes.remove(recipe)  # Remover la receta de las favoritas
            db.session.commit()  # Confirmar cambios en la base de datos
