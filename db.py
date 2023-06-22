from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import errors

from config import uri
import random


client = MongoClient(uri, server_api=ServerApi('1'))

main_database = client.tasks
shoppingList = main_database['task']


def create_task(task: str, username: str):
    try:
        shoppingList.insert_one({'_id': random.randint(1, 9999), 'task': task, 'telegram-name': username})
    except errors.DuplicateKeyError:
        shoppingList.insert_one({'_id': random.randint(1, 9999), 'task': task, 'telegram-name': username})


def get_tasks():
    users = []
    for i in shoppingList.find():
        users.append(i['task'])
        users.append(i['telegram-name'])
        users.append(i['_id'])
        
    return users


def remove_task(id: int):
    shoppingList.delete_one({'_id': id})
    return True
