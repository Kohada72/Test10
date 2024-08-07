﻿'''----------------------------------------------------------------- 
File Name		: edit_ingredients.py
Version		: V1.0 
Designer		: 上之山 将太
Date			: 2024.06.11
Purpose       	: データベースの処理をする関数を呼び出し、食材リストの管理
--------------------------------------------------------------------'''

'''
Revision : 
V1.0 : 上之山 将太, 2024.06.11
v1.1 : 上之山 将太, 2024.06.16 to_romaji
V1.2 : 上之山 将太, 2024.07.09 editIngredient
修正をした場合は以下の通りに記述をお願いします
(例)
V1.1 : 上之山 将太, 2024.06.16 to_romaji
V1.2 : 上之山 将太, 2024.07.09 editIngredient
                ・
                ・
                ・
'''

from db_edit_ingredients import dbAddIngredient, dbDeleteIngredient
import csv
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import pykakasi
import Levenshtein
#import unittest
#from mock import patch
#from get_ingredients_list import getIngredientsList
    
'''-------------------------------------------------------------------- 
Function Name       : editIngredient()
Designer            : 上之山 将太
Date                : 2024.07.09
Function            : データベースへ食材情報とユーザ情報を追加する関数の呼び出し
Argument            : id, ingredients, is_delete
Return              : なし
----------------------------------------------------------------------'''



# pykakasiのインスタンスを作成
kakasi = pykakasi.kakasi()

def to_romaji(text):
    result = kakasi.convert(text)
    return ''.join([item['hepburn'] for item in result])

def editIngredient(id, ingredients, is_delete):
    if not is_delete:  # 削除ではないなら
        new_ingredients = []

        filename = 'update_ingredient.csv'

        # encoding='shift-JIS'かも
        with open(filename, encoding='utf-8', newline='') as f:
            csvreader = csv.reader(f)
            next(csvreader)  # 最初の行をスキップ
            csv_data = {to_romaji(row[0]): int(row[1]) for row in csvreader}
        
        threshold = 0.7  # 近似度の閾値（0から1の間） カンの数値

        # 現在の日付を取得
        current_date = datetime.now()
        for ingredient in ingredients:
            name = to_romaji(ingredient['name'])
            ingredient['expiry_date'] = current_date.strftime('%Y/%m/%d')
            for key in csv_data:
                similarity = Levenshtein.ratio(key, name)
                if similarity >= threshold:  # 近似度をチェック
                    
                    # CSVファイルのデータを日、月、年に変換
                    days_to_add = csv_data[key]
                    years = days_to_add // 365
                    months = (days_to_add % 365) // 30
                    days = (days_to_add % 365) % 30
                    # 賞味期限を加算
                    new_expiry_date = current_date + relativedelta(years=years, months=months, days=days)
                    # 新しいexpiry_dateを元の形式に変換して更新
                    ingredient['expiry_date'] = new_expiry_date.strftime('%Y/%m/%d')
                    break  # 最初に一致したものを使用
            if ingredient['expiry_date'] == current_date.strftime('%Y/%m/%d'):
                ingredient['expiry_date'] = '賞味期限なし'

            new_ingredients.append(ingredient)

        # print(new_ingredients)

        dbAddIngredient(id, new_ingredients)
    else:  # 削除なら
        dbDeleteIngredient(id, ingredients)
#テストデータ
# ingredients = [
#             {
#                 #本来は"name" : "food_name",
#                 "name": "ウンチ",
#                 "quantity": 5,
#                 "unit":"個",
#                 "expiry_date" : "2024/07/09"
#             },
#             {
#                 "name": "トマト",
#                 "quantity": 1,
#                 "unit":"pc",
#                 "expiry_date" : "2024/06/12"
#             }
#         ]
# editIngredient("2", ingredients, False)

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

