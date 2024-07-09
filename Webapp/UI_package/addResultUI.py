from flask import Flask, render_template, request, session
from edit_ingredients import editIngredient
'''-------------------------------------------------------------------- 
Function Name       : normalResult
Designer            : 上之山 将太
Date                : 2024.06.02
Function            : W5 追加確認画面を表示する
Argument            : なし
Return              : render_template('result.html', food_name = name, quantity = quantity, unit = unit)
----------------------------------------------------------------------'''

def addResultUI():
    ingredients = []
    names = request.form.getlist('name')
    quantities = request.form.getlist('quantity')
    units = request.form.getlist('unit')

    for name, quantity, unit in zip(names, quantities, units):
        ingredients.append({
            "name": name,
            "quantity": quantity,
            "unit": unit,
            "expiry_date": "2024/06/12" # 賞味期限に関しては後で実装する
        })
    id = session["user_id"]
    is_delete = False #削除ではなくて追加のメソッドを読み出す
    print(names)
    editIngredient(id, ingredients, is_delete) #本来は追加処理をした後に結果を表示する
    return render_template('result.html', ingredients=ingredients)