'''----------------------------------------------------------------- 
File Name		: UI_main.py
Version		    : V1.0 
Designer		: 上之山 将太
Date			: 2024.05.27
Purpose       	: アプリケーションの画面の表示
--------------------------------------------------------------------'''

'''
Revision : 
V1.0 : 上之山 将太, 2024.05.27
v1.1 : 上之山 将太, 2024.06.16 DeleteIngredient
修正をした場合は以下の通りに記述をお願いします
(例)
V1.1 : 修正者名, 2024.06.28 改訂モジュール名
V1.2 : 修正者名, yyyy.mm.dd 改訂モジュール名
'''


from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
#from flask_sqlalchemy import SQLAlchemy
#from db_operation import get_user, add_user, get_user_ingredients, get_user_name
from get_ingredients_list import getIngredientsList, getUserName
from edit_ingredients import editIngredient, dbDeleteIngredient
import os
from db_operation import get_db, getCollection


#flaskのお決まりの構文
app = Flask(__name__)

#画像をアップロードするテストで使用したもの
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # ディレクトリが存在しない場合は作成
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#------------------------------------------------------------------------------------

'''-------------------------------------------------------------------- 
Function Name       : foodManagementUI
Designer            : 上之山 将太
Date                : 2024.05.27
Function            : W2 食材管理画面を表示する
Argument            : なし
Return              : render_template('index.html', ingredients = ingredients, user_name = user_name)
----------------------------------------------------------------------'''
#食材管理画面をルート画面としている
@app.route('/')
def foodManagementUI():
    ingredients= getIngredientsList()
    user_name = getUserName(1)
    return render_template('index.html', ingredients = ingredients, user_name = user_name)


'''-------------------------------------------------------------------- 
Function Name       : addFoodUI
Designer            : 上之山 将太
Date                : 2024.05.27
Function            : W3 食材追加画面を表示する
Argument            : なし
Return              : render_template('addFoodUI.html')
----------------------------------------------------------------------'''
@app.route('/add')
def addFoodUI():
    return render_template('addFoodUI.html')


'''-------------------------------------------------------------------- 
Function Name       : edit
Designer            : 上之山 将太
Date                : 2024.06.11
Function            : W2.1 食材管理画面(編集モード)を表示する
Argument            : なし
Return              : render_template('edit.html', ingredients = ingredients, user_name = user_name)
----------------------------------------------------------------------'''
@app.route('/edit')
def edit():
    ingredients= getIngredientsList()
    user_name = getUserName(1)
    return render_template('edit.html', ingredients = ingredients, user_name = user_name)


'''-------------------------------------------------------------------- 
Function Name       : imageRecognitionUI
Designer            : 上之山 将太
Date                : 2024.05.27
Function            : W4 画像認証画面を表示する
Argument            : なし
Return              : render_template('imageRecognition.html')
----------------------------------------------------------------------'''
@app.route('/add/ocr/')
def imageRecognitionUI():
    return render_template('imageRecognition.html')


'''-------------------------------------------------------------------- 
Function Name       : normalWay
Designer            : 上之山 将太
Date                : 2024.06.02
Function            : 手動入力による食材の追加をする画面を表示する
Argument            : なし
Return              : render_template('addNormal.html')
----------------------------------------------------------------------'''
@app.route('/add/normal/')
def normalWay():
    return render_template('addNormal.html')


'''-------------------------------------------------------------------- 
Function Name       : normalResult
Designer            : 上之山 将太
Date                : 2024.06.02
Function            : W5 追加確認画面を表示する
Argument            : なし
Return              : render_template('result.html', food_name = name, quantity = quantity, unit = unit)
----------------------------------------------------------------------'''
@app.route('/result', methods = ['POST'])
def normalResult():
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
    id = 1
    is_delete = False #削除ではなくて追加のメソッドを読み出す
    editIngredient(id, ingredients, is_delete)
    return render_template('result.html', ingredients=ingredients)
    

'''-------------------------------------------------------------------- 
Function Name       : resultUI
Designer            : 上之山 将太
Date                : 2024.05.27
Function            : 画像認証に使う画像のアップロードをし、その結果を表示する
Argument            : なし
Return              : render_template('result.html', food_name = name, quantity = quantity, unit = unit)
----------------------------------------------------------------------'''
#画像をデータベースにアップロードする関数が分からないのでいったん自分のPCに保存する
@app.route('/upload', methods=['POST'])
def resultUI():
    if 'image' not in request.files:
        return redirect(request.url)
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        #return redirect(url_for('uploaded_file', filename=file.filename))
        return render_template('result.html')


'''-------------------------------------------------------------------- 
Function Name       : deleteIngredients
Designer            : 上之山 将太
Date                : 2024.06.15
Function            : 食材管理リストの食材を削除する関数を呼び出し、食材管理画面を表示する
Argument            : なし
Return              : render_template('index.html', ingredients = ingredients, user_name = user_name)
----------------------------------------------------------------------'''
@app.route('/delete_ingredients', methods=['POST'])
def deleteIngredients():
    ingredients_to_delete = request.form.getlist('ingredients')
    is_delete = True
    id = 1
    editIngredient(id, ingredients_to_delete, is_delete)
    #削除後の食材管理リストを表示
    ingredients = getIngredientsList()
    user_name = getUserName(1)
    #expiry_date = datetime.date.today + 10 # "+10" は賞味期限を考慮したため正しい値はあとで
    return render_template('index.html', ingredients = ingredients, user_name = user_name)


#test用の関数
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return f'ファイル {filename} が正常にアップロードされました！' 

#実行する
if __name__ == '__main__':
    app.run(debug = True)




