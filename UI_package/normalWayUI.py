'''-------------------------------------------------------------------- 
Function Name       : normalWay
Designer            : 上之山 将太
Date                : 2024.06.02
Function            : 手動入力による食材の追加をする画面を表示する
Argument            : なし
Return              : render_template('addNormal.html')
----------------------------------------------------------------------'''
from flask import Flask, render_template


def normalWayUI():
    
    return render_template('addNormal.html')