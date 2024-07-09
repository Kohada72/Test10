#import recipeSearchModule
from flask import Flask, render_template,request,session
from collect_recipe_data import getRecipe, RECIPE
import pykakasi

'''-------------------------------------------------------------------- 
Function Name       : recipeListUI
Designer            : 人見 淳史
Date                : 2024.06.04
Function            : 検索で得られたレシピの一覧の画面を表示する。
Argument            : なし
Return              : render_template('recipe_list.html', rcl = recipe_lsit)
----------------------------------------------------------------------'''

#レシピ一覧画面表示処理
def recipeListUI(ingredient_list):
    ingredients = []
    kakasi = pykakasi.kakasi()
    
    #辞書型から名前要素だけを取り出してリストにする
    for ingredient in ingredient_list:
        
        roma = kakasi.convert(ingredient)
        
        #ローマ字変換
        roma_name = ""
        for i in roma:
            roma_name += i["passport"]
        
        #材料名をリストに追加
        ingredients.append(roma_name)
            
    #レシピリストを取得
    recipe_list = getRecipe(ingredients)
    
        
    return render_template("recipe_list.html", rcl = recipe_list)