from pymongo import MongoClient
from bson.objectid import ObjectId

def get_db():
    uri = "mongodb+srv://al22005:pOSrTuopGEEhSU6E@cluster0.16pm7pd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(uri)
    #user_management_listというcollectionを返している
    return client['user_management_list']

# ユーザーの情報を取得する関数
def get_user():
    id = 1  #本来はIDは引数で受け取る
    db = get_db()    #データベースを取得
    collection = db['users']    #コレクションの名前をusersにする
    return collection.find_one({"_id" : id})

def getCollection():
    db = get_db()    #データベースを取得
    collection = db['users']    #コレクションの名前をusersにする
    return collection

def edit_collection():
    collection = getCollection()
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
    
# ユーザーを追加する関数

def add_user():
    db = get_db()
    collection = db['users']
    user_with_ingredients = {
        "_id": 1,
        "username": "user3",
        "ingredients": [
            {
                "name": "beef",
                "quantity": 10,
                "unit":"g",
                "expiry_date":"2024/06/12"

            },
            {
                "name": "radish",
                "quantity": 3,
                "unit":"本",
                "expiry_date":"2024/06/12"
            }
        ]
    }
    collection.insert_one(user_with_ingredients)

# ユーザーを削除する関数
'''
def delete_user(user_id):
    db = get_db()
    collection = db['users']
    collection.delete_one({'_id': ObjectId(user_id)})

# ユーザーを更新する関数
def update_user(user_id, new_username):
    db = get_db()
    collection = db['users']
    collection.update_one({'_id': ObjectId(user_id)}, {'$set': {'username': new_username}})

'''

#食材の情報を取得
def get_user_ingredients(user_id):
    db = get_db()
    collection = db['users']
    user = collection.find_one({"_id": user_id})
    if user and "ingredients" in user:
        return user["ingredients"]
    else:
        return []

def get_user_name(user_id):
    db = get_db()
    collection = db['users']
    user = collection.find_one({"_id": user_id})
    if user and "username" in user:
        return user["username"]
    else:
        return []
    
#テスト用の関数　
# 本来はいらない関数
def get_user_id(user_name):
    db = get_db()
    collection = db['users']
    user = collection.find_one({"name": user_name})
    if user and "_id" in user:
        return user["_id"]
    else:
        return []

