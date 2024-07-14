from flask import Flask, render_template

'''-------------------------------------------------------------------- 
Function Name       : imageRecognitionUI
Designer            : 上之山 将太
Date                : 2024.05.27
Function            : W4 画像認証画面を表示する
Argument            : なし
Return              : render_template('imageRecognition.html')
----------------------------------------------------------------------'''

def imageRecognitionUI():
    return render_template('imageRecognition.html')