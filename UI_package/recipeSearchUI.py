'''-------------------------------------------------------------------- 
Function Name       : recipeListUI
Designer            : 人見 淳史
Date                : 2024.06.04
Function            : 検索するために食材を選ぶ。
Argument            : なし
Return              : render_template('recipe_list.html', rcl = recipe_lsit)
----------------------------------------------------------------------'''

from flask import session, render_template
from get_ingredients_list import getIngredientsList


#レシピ検索画面
def recipeSearchUI():
    
    id = session["user_id"]
    
    return render_template("recipeSearch.html", ingredients = getIngredientsList(id))