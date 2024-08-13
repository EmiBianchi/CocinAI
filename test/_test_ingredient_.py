from models.ingredient import Ingredient

def test_create_ingredient():
    # Prueba para verificar que se puede crear un ingrediente
    ingredient = Ingredient(name="Sugar", unit_measurement="grams")
    db.session.add(ingredient)
    db.session.commit()

    assert ingredient.id is not None  # Verificar que el ingrediente tiene un ID
    assert ingredient.name == "Sugar"  # Verificar que el nombre es correcto
    assert ingredient.unit_measurement == "grams"  # Verificar que la unidad de medida es correcta
