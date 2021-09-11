from utility.config import *
import json
from service.async_http import AsyncHttp
import re

def get_url(uri):
     base_url = get_mealdb_api_base_url()
     return base_url + uri
def get_api(uri, method, data = None, processor = None):
    def api():
        url = get_url(uri)
        response = requests.get(url)
        if response.status_code != 200:
            print(response)
            return None
        
        if processor == None:
            return response.json()
        
        return processor(response.json())
    return api

def get_default_processor(response_index):
    return lambda response: iterate_response(response, response_index, lambda item: item)

def iterate_response(response, key, processor):
    items = response.get(key, [])
    if items == None:
        return []
    item_arr = []
    for item in items:
        item_arr.append(processor(item))
    return item_arr

def ingredient_processor(response):
    return iterate_response(response, 'meals', lambda ingredient: {
        **ingredient,
        'strIngredientThumb': get_ingredient_thumbnail(ingredient['strIngredient']),
        'strIngredientThumbSmall': get_ingredient_thumbnail(ingredient['strIngredient']),
    })

def meal_processor(response):
    return iterate_response(response, 'meals', lambda meal: {
        **meal,
        'strMealThumbSmall': get_meal_thumbnail_small(meal['strMealThumb']),
    })
def meal_detail_processor(response):
    meals = meal_processor(response)
    if len(meals) > 0:
        return meals[0]

def get_meal_thumbnail_small(thumb):
    return thumb+'/preview'

def get_ingredient_thumbnail(ingredient):
    return 'https://www.themealdb.com/images/ingredients/{}.png'.format(ingredient)

def get_ingredient_thumbnail_small(ingredient):
    return 'https://www.themealdb.com/images/ingredients/{}-Small.png'.format(ingredient)

def list_items(list_type, processor):
    api = get_api('/list.php?{}=list'.format(list_type), 'GET', processor=processor)
    return api()

def list_categories():
    return list_items('c', get_default_processor('meals'))

def list_areas():
    return list_items('a', get_default_processor('meals'))

def list_ingredients():
    return list_items('i', ingredient_processor)

def all_categories():
    api = get_api('/categories.php', 'GET', processor=get_default_processor('categories'))
    return api()

def filter_by(filter_type, filter, processor):
    api = get_api('/filter.php?{}={}'.format(filter_type, filter), 'GET', processor=processor)
    return api()

def filter_by_area(area):
    return filter_by('a', area, meal_processor)

def filter_by_category(category):
    return filter_by('c', category, meal_processor)

def filter_by_ingredient(ingredient):
    return filter_by('i', ingredient, meal_processor)

def get_meal_detail(meal_id):
    api = get_api('/lookup.php?i={}'.format(meal_id), 'GET', processor=meal_detail_processor)
    return api()

def get_no_of_meals_by_area(process = None):
    areas = list_areas()
    urls = []
    url_area = {}
    for area in areas:
        uri = '/filter.php?a={}'.format(area['strArea'])
        url = get_url(uri)
        urls.append(url)
        url_area[url] = area
    meals_by_area = []
    def parse_response(response):
        data = json.loads(response.body)
        meals = meal_processor(data)
        area = url_area[response.effective_url]
        record = [area, len(meals)] if process == None else process(area, meals)
        if record != None:
            meals_by_area.append(record)
    client = AsyncHttp(urls, parse_response)
    client.start()
    return meals_by_area
    
def get_meals_by_ingredients(ingredients):
    urls = [get_url('/filter.php?i={}'.format(ingredient)) for ingredient in ingredients]
    meals = []
    client = AsyncHttp(urls, lambda response: meals.extend(meal_processor(json.loads(response.body))))
    client.start()

    meal_details_urls = [get_url('/lookup.php?i={}'.format(meal['idMeal'])) for meal in meals]
    meal_details = []
    client = AsyncHttp(meal_details_urls, lambda response: meal_details.extend(meal_processor(json.loads(response.body))))
    client.start()
    return meal_details

def search_meals(pattern):
    meal_details_urls = []
    def find_meal(area, meals):
        p = re.compile(pattern, re.IGNORECASE)
        for meal in meals:
            if p.match(meal['strMeal']) != None:
                meal_details_urls.append(get_url('/lookup.php?i={}'.format(meal['idMeal'])))
    get_no_of_meals_by_area(find_meal)

    meal_details = []
    client = AsyncHttp(meal_details_urls, lambda response: meal_details.extend(meal_processor(json.loads(response.body))))
    client.start()
    return meal_details

# "idMeal": "52772",
# "strMeal": "Teriyaki Chicken Casserole",
# "strDrinkAlternate": null,
# "strCategory": "Chicken",
# "strArea": "Japanese",
# "strInstructions": ""
# "strMealThumb": "https://www.themealdb.com/images/media/meals/wvpsxx1468256321.jpg",
# "strTags": "Meat,Casserole",
# "strYoutube": "https://www.youtube.com/watch?v=4aZr5hZXP_s",
# "strIngredient1": "soy sauce",
# "strIngredient2": "water",
# "strIngredient3": "brown sugar",
# "strIngredient4": "ground ginger",
# "strIngredient5": "minced garlic",
# "strIngredient6": "cornstarch",
# "strIngredient7": "chicken breasts",
# "strIngredient8": "stir-fry vegetables",
# "strIngredient9": "brown rice",
# "strIngredient10": "",
# "strIngredient11": "",
# "strIngredient12": "",
# "strIngredient13": "",
# "strIngredient14": "",
# "strIngredient15": "",
# "strIngredient16": null,
# "strIngredient17": null,
# "strIngredient18": null,
# "strIngredient19": null,
# "strIngredient20": null,
# "strMeasure1": "3/4 cup",
# "strMeasure2": "1/2 cup",
# "strMeasure3": "1/4 cup",
# "strMeasure4": "1/2 teaspoon",
# "strMeasure5": "1/2 teaspoon",
# "strMeasure6": "4 Tablespoons",
# "strMeasure7": "2",
# "strMeasure8": "1 (12 oz.)",
# "strMeasure9": "3 cups",
# "strMeasure10": "",
# "strMeasure11": "",
# "strMeasure12": "",
# "strMeasure13": "",
# "strMeasure14": "",
# "strMeasure15": "",
# "strMeasure16": null,
# "strMeasure17": null,
# "strMeasure18": null,
# "strMeasure19": null,
# "strMeasure20": null,
# "strSource": null,
# "strImageSource": null,
# "strCreativeCommonsConfirmed": null,
# "dateModified": null