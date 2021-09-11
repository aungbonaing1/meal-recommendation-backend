from service.mealdb import list_ingredients
from db.seed.seed_areas import seed_default_arr

def seed_ingredients():
    ingredients = list_ingredients()
    seed_default_arr('ingredients', ingredients)