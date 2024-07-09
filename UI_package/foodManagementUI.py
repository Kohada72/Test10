'''-------------------------------------------------------------------- 
Function Name       : foodManagementUI
Designer            : 上之山 将太
Date                : 2024.05.27
Function            : W2 食材管理画面を表示する
Argument            : なし
Return              : render_template('index.html', ingredients = ingredients, user_name = user_name)
----------------------------------------------------------------------'''

from flask import Flask, render_template
from get_ingredients_list import getIngredientsList



def foodManagementUI():
    ingredients= getIngredientsList()
    
    return render_template('index.html', ingredients = ingredients)

