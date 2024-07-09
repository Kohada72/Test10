'''----------------------------------------------------------------- 
File Name		: db_edit_ingredients.py
Version		: V1.0 
Designer		: 上之山 将太
Date			: 2024.06.11
Purpose       	: データベースの食材情報とユーザ情報の編集
--------------------------------------------------------------------'''

from db_operation import getCollection

'''-------------------------------------------------------------------- 
Function Name       : dbAddIngredient
Designer            : 上之山 将太
Date                : 2024.06.11
Function            : データベースへ食材情報とユーザ情報を追加
Argument            : id, ingredients
Return              : なし
----------------------------------------------------------------------'''

def dbAddIngredient(id, ingredients):
    collection = getCollection()
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
    
    for ingredient_name in ingredients_to_delete:
        collection.update_one(
            {'_id': id},
            {'$pull': {'ingredients': {'name': ingredient_name}}}
        )
