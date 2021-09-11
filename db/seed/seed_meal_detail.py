from service.mealdb import  *
from db.seed.seed_areas import seed_default_arr
from utility.dynamodb import scan, batch_itr
from utility.collection import get_dynamodb_put_request_dict

def seed_meal_detail():
    meal_ids = scan('meals', lambda x: x['idMeal']['S'])
    save_batch = lambda ids: seed_default_arr('meals', [get_meal_detail(id) for id in ids])
    batch_itr(meal_ids, save_batch)
