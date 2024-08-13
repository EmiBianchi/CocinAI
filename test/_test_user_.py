import pytest
from app import db
from models.user import User
from models.recipe import Recipe

@pytest.fixture
def user():
    # Fixture que crea un usuario para las pruebas
    user = User(name="Test User", email="test@example.com", password="hashed_password")
    db.session.add(user)
    db.session.commit()
    return user

@pytest.fixture
def recipe():
    # Fixture que crea una receta para las pruebas
    recipe = Recipe(title="Test Recipe", instructions="Mix ingredients", preparation_time=15)
    db.session.add(recipe)
    db.session.commit()
    return recipe

def test_create_user():
    # Prueba para verificar que se puede crear un usuario
    user = User(name="Test User", email="test@example.com", password="hashed_password")
    db.session.add(user)
    db.session.commit()

    assert user.id is not None  # Verificar que el usuario tiene un ID
    assert user.name == "Test User"  # Verificar que el nombre es correcto
    assert user.email == "test@example.com"  # Verificar que el email es correcto

def test_save_favorite_recipe(user, recipe):
    # Prueba para verificar que se puede guardar una receta como favorita
    user.save_favorite_recipe(recipe)
    assert recipe in user.favorite_recipes  # Verificar que la receta está en los favoritos

def test_remove_favorite_recipe(user, recipe):
    # Prueba para verificar que se puede eliminar una receta de favoritos
    user.save_favorite_recipe(recipe)  # Guardar la receta como favorita
    user.remove_favorite_recipe(recipe)  # Eliminar la receta de favoritos
    assert recipe not in user.favorite_recipes  # Verificar que la receta ya no está en favoritos
