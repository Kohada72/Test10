"""----------------------------------------------------------------------
File Name       : get_recipe.py
Version         : V1.1
Designer        : 上之山将太, 和田一真
Date            : 2024.06.27
Purpose         : 食材名およびレシピIDからレシピデータを抽出する.
----------------------------------------------------------------------"""
"""
Revision :
V1.0 : 上之山将太, 2024.06.27  初期バージョン
V1.1 : 和田一真,   2024.07.01  関数(getRecipeId, getRecipeData)仕様変更
"""

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

#データベースアクセス
uri = "mongodb+srv://al22047:ht4zD2gmM8rm9nkL@cluster0.16pm7pd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  #環境依存
client = MongoClient(uri)
dbname = client['user_management_list']
collection = dbname['recipes_collection']

#特定の食材を材料に持つ料理のレシピのIDを取得する関数
def getRecipeId(ingredient_name):
    recipe_id_list = []
    all_recipes = collection.find()
    for recipe in all_recipes:
        ingredients = recipe.get("ingredients", [])
        for ingredient in ingredients:
            if ingredient["ingredient_ro"] == ingredient_name:
                recipe_id_list.append(recipe.get("_id"))

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
