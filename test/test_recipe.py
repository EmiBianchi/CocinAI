from app.models import Recipe, Ingredient
from app import db
import unittest
from flask import current_app
from app import create_app, db

recipe = Recipe()

class RecipeTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_recipe(self):
        # Prueba para verificar que se puede crear una receta
        recipe.title ="Test Recipe"
        recipe.instructions="Mix ingredients"
        recipe.preparation_time=15
        db.session.add(recipe)
        db.session.commit()

    def test_add_ingredient_to_recipe(self):
        # Prueba para verificar que se puede agregar un ingrediente a una receta
        ingredient = Ingredient(name="Sugar", unit_measurement="grams")
        db.session.add(ingredient)
        db.session.commit()

        recipe = Recipe(title="Test Recipe", instructions="Mix ingredients", preparation_time=15)
        db.session.add(recipe)
        db.session.commit()

        recipe.add_ingredient(ingredient, 100)  # Agregar el ingrediente a la receta
        self.assertEqual(len(recipe.ingredients), 1)  # Verificar que la receta tiene un ingrediente
        self.assertEqual(recipe.ingredients[0].name, "Sugar")  # Verificar que el ingrediente agregado es correcto
    def test_remove_ingredient_from_recipe(self):
        # Prueba para verificar que se puede eliminar un ingrediente de una receta
        ingredient = Ingredient(name="Sugar", unit_measurement="grams")
        db.session.add(ingredient)
        db.session.commit()

        recipe = Recipe(title="Test Recipe", instructions="Mix ingredients", preparation_time=15)
        db.session.add(recipe)
        db.session.commit()

        recipe.add_ingredient(ingredient, 100)  # Agregar el ingrediente a la receta
        recipe.remove_ingredient(ingredient)  # Eliminar el ingrediente de la receta
        self.assertEqual(len(recipe.ingredients), 0)  # Verificar que la receta no tiene ingredientes
        self.assertIsNotNone(recipe.id)  # Verificar que la receta tiene un ID
        self.assertEqual(recipe.title, "Test Recipe")  # Verificar que el título es correcto
        self.assertEqual(recipe.preparation_time, 15)  # Verificar que el tiempo de preparación es correcto

if __name__ == '__main__':
    unittest.main()
