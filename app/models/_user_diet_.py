class UserDiet(db.Model):
    __tablename__ = 'user_diet'  # Nombre de la tabla en la base de datos

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)  # Clave foránea a User
    diet_id = db.Column(db.Integer, db.ForeignKey('diets.id'), primary_key=True)  # Clave foránea a Diet
