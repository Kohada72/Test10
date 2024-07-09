from flask import Flask, render_template
'''-------------------------------------------------------------------- 
Function Name       : addFoodUI
Designer            : 上之山 将太
Date                : 2024.05.27
Function            : W3 食材追加画面を表示する
Argument            : なし
Return              : render_template('addFoodUI.html')
----------------------------------------------------------------------'''

def addFoodUI():
    return render_template('addFood.html')