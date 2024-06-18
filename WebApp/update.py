from pymongo import MongoClient
from db_operation import get_db, getCollection


db = get_db()
collection =  getCollection()
# 更新スクリプト
for doc in collection.find():
    updated_ingredients = []
    for ingredient in doc['ingredients']:
        ingredient['unit'] = None
        ingredient['expiry_date'] = None
        updated_ingredients.append(ingredient)
    
    collection.update_one(
        {'_id': doc['_id']},
        {'$set': {'ingredients': updated_ingredients}}
    )