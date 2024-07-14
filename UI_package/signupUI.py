from flask import  render_template,redirect,flash
from db_operation import addUser
'''-------------------------------------------------------------------- 
Function Name       : signupUI
Designer            : 人見淳史
Date                : 2024.07.7
Function            : ユーザー登録をする
Argument            : なし
Return              : render_template('signup.html')
----------------------------------------------------------------------'''

def signupUI1():
    return render_template('signup.html')

def signupUI2(user_id, user_name, user_passward):
    try:
        user_id = int(user_id)
    except ValueError:
        flash("ユーザIDの欄には数値を入力して下さい")
        return redirect("/signup")
    
    if(addUser(user_id, user_name, user_passward)):
        flash("ユーザ登録が完了しました")
        return redirect("/login")
    else:
        flash("既存のユーザIDです。")
        return redirect("/signup")