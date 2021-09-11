from db.migration.create_areas_table import create_areas_table
from db.migration.create_categories_table import create_categories_table
from db.migration.create_ingredients_table import create_ingredients_table
from db.migration.create_meal_ingredients_table import create_meal_ingredients_table
from db.migration.create_meals_table import create_meals_table

def migrate_all():
    create_areas_table()
    create_categories_table()
    create_ingredients_table()
    create_meal_ingredients_table()
    create_meals_table()