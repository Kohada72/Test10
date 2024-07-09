'''----------------------------------------------------------------- 
File Name		: db_operation.py
Version		: V1.0 
Designer		: 上之山 将太
Date			: 2024.06.04
Purpose       	: データベースの食材情報とユーザ情報の編集
--------------------------------------------------------------------'''


from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


'''-------------------------------------------------------------------- 
Function Name       : getDb
Designer            : 上之山 将太
Date                : 2024.06.04
Function            : データベース自体を渡す
Argument            : なし
Return              : db
----------------------------------------------------------------------'''
def get_db():
    uri = "mongodb+srv://al22005:pOSrTuopGEEhSU6E@cluster0.16pm7pd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(uri)
    #user_management_listというデータベースを返している
    db = client['user_management_list']
    return db

'''-------------------------------------------------------------------- 
Function Name       : getUser
Designer            : 上之山 将太
Date                : 2024.06.04
Function            : idに該当するユーザの情報を返す
Argument            : id
Return              : collection
----------------------------------------------------------------------'''
# ユーザーの情報を取得する関数
def getUser(id):
    db = get_db()    #データベースを取得
    collection = db['users']    #コレクションの名前をusersにする
    return collection.find_one({"_id" : id})

'''-------------------------------------------------------------------- 
Function Name       : getCollection
Designer            : 上之山 将太
Date                : 2024.06.04
Function            : 全てのユーザの情報を返す
Argument            : なし
Return              : collection
----------------------------------------------------------------------'''
def getCollection():
    db = get_db()    #データベースを取得
    collection = db['users']    #コレクションの名前をusersにする
    return collection

#test用の関数
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
'''-------------------------------------------------------------------- 
Function Name       : addUser
Designer            : 上之山 将太
Date                : 2024.06.21
Function            : ユーザを追加する
Argument            : id, user_name, password
Return              : なし
----------------------------------------------------------------------'''
def addUser():
    #本来は引数として受け取る--------
    id = 20
    user_name = "user5"
    password = "default_password"
    #------------------------------

    db = get_db()
    collection = db['users']
    user_with_ingredients = {
        "_id": id,
        "username": user_name,
        "password" : password,
        "ingredients": []
    }

    try:
        collection.insert_one(user_with_ingredients)
        print("User inserted successfully")
    except DuplicateKeyError:
        print(f"User with _id {user_with_ingredients['_id']} already exists in the collection")
    

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
def get_user_id(password):
    db = get_db()
    collection = db['users']
    user = collection.find_one({"password": password})
    if user and "_id" in user:
        return user["_id"]
    else:
        return []

