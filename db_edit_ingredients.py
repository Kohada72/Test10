'''----------------------------------------------------------------- 
File Name		: db_edit_ingredients.py
Version		: V1.1 
Designer		: 上之山 将太
Date			: 2024.07.02
Purpose       	: データベースの食材情報とユーザ情報の編集
--------------------------------------------------------------------'''

'''
Revision : 
V1.0 : 上之山 将太, 2024.06.11
修正をした場合は以下の通りに記述をお願いします
(例)
V1.1 : 上之山将太, 2024.07.02 dbDeleteIngredient
'''

from db_operation import getCollection, addUser, getDb


'''-------------------------------------------------------------------- 
Function Name       : dbAddIngredient
Designer            : 上之山 将太
Date                : 2024.06.11
Function            : データベースへ食材情報とユーザ情報を追加
Argument            : id, ingredients(リスト型)
Return              : なし
----------------------------------------------------------------------'''

def dbAddIngredient(id, ingredients):
    collection = getCollection()
    #user_id == id　のユーザがいるかどうか 
    if not collection.find_one({"_id": id}):
        raise ValueError(f"ユーザID {id} がデータベースに存在しません")

    if not isinstance(ingredients, list) or not all(isinstance(ingredient, dict) for ingredient in ingredients):
        raise ValueError("ingredientsは辞書型のリストでなければなりません")
    
    for ingredient in ingredients:
        # 食材の追加
        collection.update_one(
            {"_id": id},
            {"$push": {"ingredients": ingredient}}
        )

# def dbDeleteIngredient(id, ingredient_name):
#     collection = getCollection
#     # 削除したいingredientの情報
#     id = "3"
#     ingredient_name = "beef"

#     # ingredients配列から特定のingredientを削除
#     collection.update_one(
#         {"_id": id},
#         {"$pull": {"ingredients": {"name": ingredient_name}}}
#     )

'''-------------------------------------------------------------------- 
Function Name       : dbDeleteIngredient
Designer            : 上之山 将太
Date                : 2024.07.02
Function            : データベースの食材情報を削除
Argument            : id, ingredients_to_delete
Return              : なし
----------------------------------------------------------------------'''

def dbDeleteIngredient(id, ingredients_to_delete):
    collection = getCollection()
    if not collection.find_one({"_id": id}):
        raise ValueError(f"ユーザID {id} がデータベースに存在しません")

    if not isinstance(ingredients_to_delete, list) or not all(isinstance(ingredient, dict) for ingredient in ingredients_to_delete):
        raise ValueError("ingredientsは辞書型のリストでなければなりません")
    # ingredients_to_delete = request.form.getlist('ingredients')
    for ingredient in ingredients_to_delete:
        #削除する食材の検索条件が食材名だけだと同じ食材をすべて削除してしまうので、賞味期限も条件に追加
        ingredient_name = ingredient['name']
        expiry_date = ingredient['expiry_date']
        collection.update_one(
            {'_id': id},
            {'$pull': {'ingredients': {'name': ingredient_name, 'expiry_date' : expiry_date}}}
        )



'''-------------------------------------------------------------------- 
Function Name       : addUserIngredients
Designer            : 上之山 将太
Date                : 2024.06.21
Function            : ユーザを追加する
Argument            : user_id
Return              : ingredients
----------------------------------------------------------------------'''
#食材の情報を取得
def getUserIngredients(user_id):
    db = getDb()
    collection = db['users']
    user = collection.find_one({"_id": user_id})
    if user and "ingredients" in user:
        ingredients = user["ingredients"]
        return ingredients
    else:
        return []


'''------テストデータ---------------------------
ingredients = [
    {
        "name": "beef",
        "quantity": 10,
        "unit":"g",
        "expiry_date":"2024/07/12"
    },
    {
        "name": "トマト",
        "quantity": 10,
        "unit":"kg",
        "expiry_date":"2024/07/12"
    }
]


ingredient = [
    {
        "name": "bread",
        "quantity": 10,
        "unit":"枚",
        "expiry_date":"2024/07/12"
    }
]


id = "20"
user_name = "user5"
password = "default_password"
#addUser(id, user_name, password)
#dbAddIngredient(id, ingredient)
dbDeleteIngredient(id, ingredient)
---------------------------------------'''
# ingredient = [
#     {
#         "name": "bread",
#         "quantity": 10,
#         "unit":"枚",
#         "expiry_date":"2024/07/12"
#     }
# ]
# id = '100000'
# dbAddIngredient(id, ingredient)
# dbDeleteIngredient(id, ingredient)