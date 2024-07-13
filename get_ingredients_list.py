'''----------------------------------------------------------------- 
File Name		: get_ingredients_list.py
Version		: V1.0 
Designer		: 上之山 将太
Date			: 2024.06.11
Purpose       	: データベースから食材管理情報とユーザ名を取得する
--------------------------------------------------------------------'''

'''
Revision : 
V1.0 : 上之山 将太, 2024.06.11
修正をした場合は以下の通りに記述をお願いします
(例)
V1.1 : 修正者名, 2024.06.28 改訂モジュール名
V1.2 : 修正者名, yyyy.mm.dd 改訂モジュール名
'''



'''-------------------------------------------------------------------- 
Function Name       : getIngredientsList()
Designer            : 上之山 将太
Date                : 2024.06.11
Function            : データベースから食材管理情報を取得する
Argument            : id
Return              : ingredients
----------------------------------------------------------------------'''
from db_operation import getUser
from db_edit_ingredients import getUserIngredients

def getIngredientsList(id):
    #本来はいらない
    user = getUser(id)
    #print(user['_id'])
    ingredients = getUserIngredients(user['_id'])
    #ingredients(食材の情報)を返す。
    return  ingredients


#print(getIngredientsList())

'''
def getUserName(id):
    user = get_user()
    user_name = get_user_name(user['_id'])
    #ユーザ名を返す。
    return user_name
'''