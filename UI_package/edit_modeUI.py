from flask import Flask, render_template
from get_ingredients_list import getIngredientsList

'''-------------------------------------------------------------------- 
Function Name       : edit
Designer            : 上之山 将太
Date                : 2024.06.11
Function            : W2.1 食材管理画面(編集モード)を表示する
Argument            : なし
Return              : render_template('edit.html', ingredients = ingredients, user_name = user_name)
----------------------------------------------------------------------'''

def edit_modeUI():
    ingredients= getIngredientsList()

    return render_template('edit.html', ingredients = ingredients)