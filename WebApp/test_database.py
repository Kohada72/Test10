from pymongo import MongoClient

def get_db():
    uri = "mongodb+srv://al22005:pOSrTuopGEEhSU6E@cluster0.16pm7pd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(uri)
    return client['user_management_list']

# ユーザーを全て取得する関数
def get_user():
    db = get_db()    #データベースを取得
    collection = db['users']    #コレクションの名前をusersにする
    return collection.find({'_id' : 'user_id_1'})

# ユーザーを追加する関数
def add_user(food_name, food_num):
    db = get_db()
    collection = db['users']
    user_with_ingredients = {
        "_id": "user_id_1",
        "username": "user1",
        "ingredients": [
            {
                #本来は"name" : "food_name",
                "name": "tomato",
                "num": 5,
            },
            {
                "name": "flour",
                "num": 2,
            },
            {
                "name": "milk",
                "num": 1,
            }
        ]
    }
    collection.insert_one({'user_info': user_with_ingredients})
