"""----------------------------------------------------------------------
File Name       : get_recipe.py
Version         : V1.0
Designer        : 和田一真
Date            : 2024.07.02
Purpose         : 抽出されたレシピのデータをクラスとして保持する.
----------------------------------------------------------------------"""
"""
Revision :
V1.0 : 和田一真  2024.07.02  初期バージョン
"""

from get_recipe import getRecipeId, getRecipeData
from bson import ObjectId

class RECIPE:
    def __init__(self):
        self.recipe_name = ""
        self.recipe_uri = ""
        self.ingredient_list = {}
        self.instracts = []

def getRecipe(ingredient_names):
    tmp_id_list = []
    for i, name in enumerate(ingredient_names):
        tmp_id_list.append(getRecipeId(name))

    flat_id_list = [id for sub in tmp_id_list for id in sub]
    flat_id_list = list(set(flat_id_list))
    if len(flat_id_list) >= 20:
        get_id_list = flat_id_list[:20]
    else:
        get_id_list = flat_id_list[:len(flat_id_list)]

    recipe_list = []
    for data in getRecipeData(get_id_list):
        tmp_class = RECIPE()
        tmp_class.recipe_name = data.get('recipe_name', '')
        tmp_class.recipe_uri = str(data.get('_id', ''))
        tmp_class.ingredient_list = {
            ingredient['ingredient']: ingredient['quantity']
            for ingredient in data.get('ingredients', [])
        }
        tmp_class.instracts = [
            data['method'][key]
            for key in sorted(data['method'].keys())
        ]
        recipe_list.append(tmp_class)

    return recipe_list

def getRecipeFromUri(uri):    
    id = [ObjectId(uri)]
    recipe_data = getRecipeData(id)[0]
    recipe = RECIPE()
    recipe.recipe_name = recipe_data.get('recipe_name', '')
    recipe.recipe_uri = str(recipe_data.get('_id', ''))
    recipe.ingredient_list = {ingredient['ingredient']: ingredient['quantity']
            for ingredient in recipe_data.get('ingredients', [])}
    recipe.instracts = [
        recipe_data['method'][key]
        for key in sorted(recipe_data['method'].keys())
    ]
    return recipe
