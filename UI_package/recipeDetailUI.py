from flask import Flask, render_template
from collect_recipe_data import getRecipeFromUri, RECIPE

'''-------------------------------------------------------------------- 
Function Name       : recipeDetailUI
Designer            : 人見 淳史
Date                : 2024.06.06
Function            : レシピの詳細な情報を表示する画面に遷移
Argument            : なし
Return              : render_template('recipeDetail.html', recipe = recipe)
----------------------------------------------------------------------'''

def recipeDetailUI(uri):
    
    #uriからレシピ情報を取得する関数 
    recipe_data = getRecipeFromUri(uri)
    
    return  render_template("recipeDetail.html", recipe = recipe_data)