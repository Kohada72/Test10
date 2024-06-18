'''----------------------------------------------------------------- 
File Name		: edit_ingredients.py
Version		: V1.0 
Designer		: 上之山 将太
Date			: 2024.06.11
Purpose       	: データベースの食材情報とユーザ情報の編集
--------------------------------------------------------------------'''

'''
Revision : 
V1.0 : 上之山 将太, 2024.06.11
v1.1 : 上之山 将太, 2024.06.16 dbDeleteIngredient
修正をした場合は以下の通りに記述をお願いします
(例)
V1.1 : 修正者名, 2024.06.28 改訂モジュール名
V1.2 : 修正者名, yyyy.mm.dd 改訂モジュール名
'''

from pymongo import MongoClient
from flask import Flask, render_template, request
from db_operation import get_db, getCollection, get_user, get_user_name
from get_ingredients_list import getIngredientsList


'''-------------------------------------------------------------------- 
Function Name       : dbAddIngredient
Designer            : 上之山 将太
Date                : 2024.06.11
Function            : データベースへ食材情報とユーザ情報を追加
Argument            : id, user_name, ingredient_name, quantity, unit, expiry_date
Return              : なし
----------------------------------------------------------------------'''

def dbAddIngredient(id, ingredients):
    db = get_db()
    collection = db['users']
    # user_name = get_user_name(id)
    # user_with_ingredients = {
    #     "_id": id,
    #     "username": user_name,
    #     "ingredients": [
    #         {
    #             #本来は"name" : "food_name",
    #             "name": ingredients["name"],
    #             "quantity": ingredients["quantity"],
    #             "unit": ingredients["unit"],
    #             "expiry_date": ingredients["expiry_date"]
    #         }
    #     ]
    # }
    for ingredient in ingredients:
        #食材の追加
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
Date                : 2024.06.16
Function            : データベースの食材情報を削除
Argument            : id, ingredients_to_delete
Return              : なし
----------------------------------------------------------------------'''

def dbDeleteIngredient(id, ingredients_to_delete):
    collection = getCollection()
    id = 1 #試験的にIDを1としている
    # ingredients_to_delete = request.form.getlist('ingredients')
    for ingredient_name in ingredients_to_delete:
        collection.update_one(
            {'_id': id},
            {'$pull': {'ingredients': {'name': ingredient_name}}}
        )

    
    
    

'''-------------------------------------------------------------------- 
Function Name       : editIngredient()
Designer            : 上之山 将太
Date                : 2024.06.11
Function            : データベースへ食材情報とユーザ情報を追加する関数の呼び出し
Argument            : id, ingredients, is_delete
Return              : なし
----------------------------------------------------------------------'''
def editIngredient(id, ingredients, is_delete):
    if is_delete == False:  #削除ではないなら
        dbAddIngredient(id, ingredients)
    else:   #削除なら
        dbDeleteIngredient(id, ingredients)
