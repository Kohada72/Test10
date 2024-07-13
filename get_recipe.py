"""----------------------------------------------------------------------
File Name       : get_recipe.py
Version         : V1.2
Designer        : 上之山将太, 和田一真
Date            : 2024.06.27
Purpose         : 食材名およびレシピIDからレシピデータを検索する.
----------------------------------------------------------------------"""
"""
Revision :
V1.0 : 上之山将太  2024.06.27  初期バージョン
V1.1 : 和田一真    2024.07.01  関数(getRecipeId, getRecipeData)仕様変更, 処理の最適化
V1.2 : 和田一真    2024.07.09  関数(getRecipeId)の検索機能の強化
"""
"""Requirement
fuzzywuzzy         0.18.0
Levenshtein        0.25.1
pymongo            4.8.0
python-Levenshtein 0.25.1
rapidfuzz          3.9.4
"""

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from fuzzywuzzy import fuzz

#データベースアクセス
uri = "mongodb+srv://web_server:h5vaahiG7WmtrgEN@cluster0.16pm7pd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  #環境依存
client = MongoClient(uri)
dbname = client['user_management_list']
collection = dbname['recipes_collection']

#特定の食材を材料に持つ料理のレシピのIDを取得する関数
def getRecipeId(ingredient_name):
    recipe_id_list = []
    all_recipes = collection.find()
    for recipe in all_recipes:
        ingredients = recipe.get("ingredients", [])
        find = False
        for ingredient in ingredients:
            tmp_ing = ingredient["ingredient_ro"]
            dif = abs(len(tmp_ing) - len(ingredient_name))
            for i in range(dif + 1):
                sli_ing = tmp_ing[i : (i + len(ingredient_name)) if len(ingredient_name) < len(tmp_ing) else len(tmp_ing)]
                sim_score = fuzz.ratio(sli_ing, ingredient_name)
                if sim_score >= 70:
                    recipe_id_list.append(recipe.get("_id"))
                    find = True
            if find:
                break

    return recipe_id_list

#該当するレシピを返す関数
def getRecipeData(all_object_id):
    recipes = []
    all_recipes = collection.find()
    for recipe in all_recipes:
        for object_id in all_object_id:
            if recipe.get("_id") == object_id:
                recipes.append(recipe)

    return recipes

"""
テストコード
recipe_id_list = getRecipeId("mitsuba")
print(getRecipeData(recipe_id_list))
"""
