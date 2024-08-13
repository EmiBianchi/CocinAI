from models.recipe import Recipe
from models.ingredient import Ingredient

@pytest.fixture
def ingredient():
    # Fixture que crea un ingrediente para las pruebas
    ingredient = Ingredient(name="Sugar", unit_measurement="grams")
    db.session.add(ingredient)
    db.session.commit()
    return ingredient

def test_create_recipe():
    # Prueba para verificar que se puede crear una receta
    recipe = Recipe(title="Test Recipe", instructions="Mix ingredients", preparation_time=15)
    db.session.add(recipe)
    db.session.commit()

    assert recipe.id is not None  # Verificar que la receta tiene un ID
    assert recipe.title == "Test Recipe"  # Verificar que el título es correcto
    assert recipe.preparation_time == 15  # Verificar que el tiempo de preparación es correcto

def test_add_ingredient_to_recipe(recipe, ingredient):
    # Prueba para verificar que se puede agregar un ingrediente a una receta
    recipe.add_ingredient(ingredient, 100)  # Agregar el ingrediente a la receta
    assert len(recipe.ingredients) == 1  # Verificar que la receta tiene un ingrediente
    assert recipe.ingredients[0].name == "Sugar"  # Verificar que el ingrediente agregado es correcto

def test_remove_ingredient_from_recipe(recipe, ingredient):
    # Prueba para verificar que se puede eliminar un ingrediente de una receta
    recipe.add_ingredient(ingredient, 100)  # Agregar el ingrediente a la receta
    recipe.remove_ingredient(ingredient)  # Eliminar el ingrediente de la receta
    assert len(recipe.ingredients) == 0  # Verificar que la receta no tiene ingredientes
