from service.mealdb import list_categories
from db.seed.seed_areas import seed_default_arr

def seed_categories():
    categories = list_categories()
    seed_default_arr('categories', categories)