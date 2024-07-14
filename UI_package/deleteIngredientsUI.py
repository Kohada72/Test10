from flask import Flask, redirect, request, session
from edit_ingredients import editIngredient
from get_ingredients_list import getIngredientsList
import json

'''-------------------------------------------------------------------- 
Function Name       : deleteIngredients
Designer            : 上之山 将太
Date                : 2024.06.15
Function            : 食材管理リストの食材を削除する関数を呼び出し、食材管理画面を表示する
Argument            : なし
Return              : render_template('index.html', ingredients = ingredients, user_name = user_name)
----------------------------------------------------------------------'''

def deleteIngredientsUI():
    ingredients_to_delete_str = request.form.getlist('ingredients')
    is_delete = True
    id = session["user_id"]
    
    
    #データを辞書型に再度変換
    ingredients_to_delete = []
    for i in ingredients_to_delete_str:
        i = i.replace("\'", "\"")
        ingredient = json.loads(i)
        ingredients_to_delete.append(ingredient)
        
    editIngredient(id, ingredients_to_delete, is_delete)
    
    #expiry_date = datetime.date.today + 10 # "+10" は賞味期限を考慮したため正しい値はあとで
    return redirect('/')