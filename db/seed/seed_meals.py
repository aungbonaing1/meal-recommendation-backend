from service.mealdb import  *
from db.seed.seed_areas import seed_default_arr
def seed_meals():
    areas = list_areas()
    meals = []
    for area in areas:
        meals = meals + filter_by_area(area['strArea'])
    seed_default_arr('meals', meals)
