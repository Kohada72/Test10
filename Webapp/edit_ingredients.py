'''----------------------------------------------------------------- 
File Name		: edit_ingredients.py
Version		: V1.0 
Designer		: 上之山 将太
Date			: 2024.06.11
Purpose       	: データベースの処理をする関数を呼び出し、食材リストの管理
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

from db_operation import get_db, getCollection
from db_edit_ingredients import dbAddIngredient, dbDeleteIngredient
#import unittest
#from mock import patch
#from get_ingredients_list import getIngredientsList


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


#mockでテスト
'''
ingredients = [
            {
                #本来は"name" : "food_name",
                "ingredient": "tomato",
                "quantity": 5,
                "unit":"個",
                "expiry_date" : "20240101"
            },
        ]
class Test_editIngredient(unittest.TestCase):
    @patch("__main__.editIngredient")
    def test_add(self, mock):
        
        editIngredient(1, ingredients, False)
        self.assertTrue(mock.called)

    @patch("__main__.editIngredient")
    def test_delete(self, mock):
        editIngredient(1, ingredients, True)
        self.assertFalse(mock.called)


if __name__ == "__main__":
    unittest.main()

'''

