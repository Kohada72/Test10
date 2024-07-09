from flask import Flask, render_template, request, redirect,app
import os

'''-------------------------------------------------------------------- 
Function Name       : resultUI
Designer            : 上之山 将太
Date                : 2024.05.27
Function            : 画像認証に使う画像のアップロードをし、その結果を表示する
Argument            : なし
Return              : render_template('result.html', food_name = name, quantity = quantity, unit = unit)
----------------------------------------------------------------------'''
#画像をデータベースにアップロードする関数が分からないのでいったん自分のPCに保存する

def recoResultUI():
    if 'image' not in request.files:
        return redirect(request.url)
    file = request.files['image']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filepath = os.path.join("uploads", file.filename)
        file.save(filepath)

        return render_template('result.html')
    
    