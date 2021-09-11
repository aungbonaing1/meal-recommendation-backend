# import inspect
import sys
from service.mealdb import *
from db.migration.migrate_all import migrate_all
from db.migration.create_areas_table import create_areas_table
from db.migration.create_categories_table import create_categories_table
from db.migration.create_ingredients_table import create_ingredients_table
from db.migration.create_meal_ingredients_table import create_meal_ingredients_table
from db.migration.create_meals_table import create_meals_table

from db.seed.seed_all import seed_all
from db.seed.seed_areas import seed_areas
from db.seed.seed_categories import seed_categories
from db.seed.seed_ingredients import seed_ingredients
from db.seed.seed_meals import seed_meals
from db.seed.seed_meal_detail import seed_meal_detail

from utility.collection import filter_by_keys

provided_cmds = [
    migrate_all,
    create_areas_table,
    create_categories_table,
    create_ingredients_table,
    create_meal_ingredients_table,
    create_meals_table,

    seed_all,
    seed_areas,
    seed_ingredients,
    seed_categories,
    seed_meals,
    seed_meal_detail,
]



# i = list_categories()
# i = list_areas()
# i = list_ingredients()
# i = all_categories()
# i = filter_by_area('Canadi')
# i = filter_by_ingredient('Dash Vegetable Oil')
# i = get_meal_detail(52772)
# print(len(i))
# print(i)

# def display_meals_by_ingradients(ingredients):
#     pass

# migrate_all()
# create_areas_table()
# create_categories_table()
# seed_areas()
# seed_ingredients()
# seed_categories()
# seed_meals()
# seed_meal_detail()

# r = inspect.getfullargspec(migrate_all)
# print(r)
def print_provided_cmds():
    print('please enter one of the cmd below:')
    for provided_cmd in provided_cmds:
        print(provided_cmd.__name__)

def exec_cmd(argv):
    if len(argv) == 1:
        print_provided_cmds()
        return
    input_cmd = argv[1]
    for provided_cmd in provided_cmds:
        if provided_cmd.__name__ == input_cmd:
            provided_cmd()
            print('executed {} successfully!'.format(input_cmd))
            return
    print_provided_cmds()

# if __name__ == '__main__':
#     exec_cmd(sys.argv)

#Display the number of meals based on area
def display_no_of_meals_by_area():
    areas = list_areas()
    no_of_meals_by_area = []
    for area in areas:
        meals = filter_by_area(area['strArea'])
        no_of_meals_by_area.append([area['strArea'], len(meals)])
    print(no_of_meals_by_area)



# display_no_of_meals_by_area()

# print(get_no_of_meals_by_area())
# ingredients = [
#     'Yukon Gold Potatoes',
#     'Beef Stock Concentrate',
#     'Chicken Breast',
#     'Chicken Breasts',
# ]
# print(get_meals_by_ingredients(ingredients))

# meals = search_meals('Chicken')
# print([filter_by_keys(meal, ['strMeal']) for meal in meals])