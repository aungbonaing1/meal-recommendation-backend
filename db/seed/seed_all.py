
from db.seed.seed_areas import seed_areas
from db.seed.seed_categories import seed_categories
from db.seed.seed_ingredients import seed_ingredients
from db.seed.seed_meals import seed_meals
from db.seed.seed_meal_detail import seed_meal_detail

def seed_all():
    seed_areas()
    seed_ingredients()
    seed_categories()
    seed_meals()
    seed_meal_detail()