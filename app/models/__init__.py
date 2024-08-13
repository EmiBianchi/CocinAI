"""
Esto es lo que estaba antes:

from .user import User
from .role import Role
from .user_data import UserData
from .profile import Profile

"""

# Importar modelos
from ._user_ import User
from ._recipe_ import Recipe
from ._ingredient_ import Ingredient
from ._diet_ import Diet
from ._user_favorite_recipe_ import UserFavoriteRecipe
from ._user_diet_ import UserDiet
from ._recipe_ingredient_ import RecipeIngredient
from ._recipe_diet_ import RecipeDiet
