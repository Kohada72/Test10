from flask import Flask, redirect, request, session
from edit_ingredients import editIngredient
from get_ingredients_list import getIngredientsList

'''-------------------------------------------------------------------- 
Function Name       : deleteIngredients
Designer            : 上之山 将太
Date                : 2024.06.15
Function            : 食材管理リストの食材を削除する関数を呼び出し、食材管理画面を表示する
Argument            : なし
Return              : render_template('index.html', ingredients = ingredients, user_name = user_name)
----------------------------------------------------------------------'''

def deleteIngredientsUI():
    ingredients_to_delete = request.form.getlist('ingredients')
    is_delete = True
    id = session["user_id"]
    editIngredient(id, ingredients_to_delete, is_delete)
    
    #削除後の食材管理リストを表示
    #ingredients = getIngredientsList()
    #user_name = getUserName(1)
    
    #expiry_date = datetime.date.today + 10 # "+10" は賞味期限を考慮したため正しい値はあとで
    return redirect('/')