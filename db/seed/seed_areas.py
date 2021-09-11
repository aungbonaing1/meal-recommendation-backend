from service.mealdb import list_areas
from utility.collection import get_dynamodb_dict_arr
from utility.dynamodb import write_batch

def seed_default_arr(table, arr):
    if len(arr) == 0:
        print('nothing to seed!')
        return
    arr = get_dynamodb_dict_arr(arr)
    try:
        write_batch(table, arr)
        print('seeded {} successfully! total records: {}'.format(table, len(arr)))
    except Exception as e:
        print('seeded {} failed!'.format(table))
        print(arr)
        print(e)

def seed_areas():
    areas = list_areas()
    seed_default_arr('areas', areas)