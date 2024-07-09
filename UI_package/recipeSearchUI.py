#import recipeSearchModule
from flask import Flask, render_template
from get_ingredients_list import getIngredientsList
'''-------------------------------------------------------------------- 
Function Name       : recipeListUI
Designer            : 人見 淳史
Date                : 2024.06.04
Function            : 検索するために食材を選ぶ。
Argument            : なし
Return              : render_template('recipe_list.html', rcl = recipe_lsit)
----------------------------------------------------------------------'''

#レシピ検索画面
def recipeSearchUI():
        
    return render_template("recipeSearch.html", ingredients = getIngredientsList())