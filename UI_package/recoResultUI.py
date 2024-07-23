'''-------------------------------------------------------------------- 
Function Name       : resultUI
Designer            : 上之山 将太
Date                : 2024.05.27
Function            : 画像認証に使う画像のアップロードをし、その結果を表示する
Argument            : なし
Return              : render_template('result.html', food_name = name, quantity = quantity, unit = unit)
----------------------------------------------------------------------'''

from flask import Flask, render_template, request, redirect,app
import os
from imageAnalysis import imageAnalysis



def recoResultUI():
    #ファイル無しはもう一度
    if 'image' not in request.files:
        return redirect("/imageReco")
    
    
    file = request.files['image']
    #ファイル名が空白の場合もう一度
    if file.filename == '':
        return redirect("/imageReco")
    #正常なアップロードの場合、画像解析に渡す
    if file:
        filepath = os.path.join("uploads", "analysis." + file.filename.rsplit('.', 1)[1].lower())
        file.save(filepath)
    
    
        #食材のデータを画像解析からもらう
        ingredient_list = imageAnalysis(filepath)
 
        
        return render_template("addNormal.html", ingredients = ingredient_list )    