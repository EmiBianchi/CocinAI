class RecipeDiet(db.Model):
    __tablename__ = 'recipe_diet'  # Nombre de la tabla en la base de datos

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), primary_key=True)  # Clave foránea a Recipe
    diet_id = db.Column(db.Integer, db.ForeignKey('diets.id'), primary_key=True)  # Clave foránea a Diet
