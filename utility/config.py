import requests
from environs import Env

def read_env():
    env = Env()
    env.read_env()
    return env

def read_str(key):
    env = read_env()
    return env(key)

def read_dict(key):
    env = read_env()
    return env.dict(var_key, subcast=str)

def read_list(key):
    env = read_env()
    return env.list(var_key)

def get_mealdb_api_base_url():
    return read_str('MEALDB_API_BASE_URL')

def get_aws_profile():
    return read_str('AWS_PROFILE')