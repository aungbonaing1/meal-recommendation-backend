from service.mealdb import *

def lambda_handler(event, context):
    result = get_no_of_meals_by_area()
    print(result)