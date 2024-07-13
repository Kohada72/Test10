from flask import Flask, render_template, request, redirect, session, flash
from UI_package import recipeListUI, addFoodUI, addResultUI, deleteIngredientsUI, edit_modeUI, foodManagementUI, \
    imageRecognitionUI, loginUI, normalWayUI, recipeDetailUI, recoResultUI, recipeSearchUI,signupUI

'''-------------------------------------------------------------------- 
Function Name       : MainUI
Designer            : 人見 淳史
Date                : 2024.05.25
Function            : 各画面の遷移を実行するモジュールを呼び出し,画面遷移を管理する。
Argument            : なし
Return              : なし
----------------------------------------------------------------------'''

#アプリケーションのセットアップ
app = Flask(__name__, static_folder='./static/')
app.config['UPLOAD_FOLDER'] = 'uploads'

#セッションのデータを暗号化
app.secret_key = '1B10'

#ページのルート設定
 
#M2ログイン画面の遷移処理
@app.route('/login', methods = ('GET', 'POST'))
def login():
    
    if "is_login" not in session:
        session['is_login'] = False
    
    if(request.method == 'GET'): #最初の遷移
        session["is_login"] = False
        return render_template('login.html')
    
    else: #二度目以降
        user_id = request.form.get('userID') #入力を受け取る
        passward = request.form.get('passward') #入力を受け取る
        
        #文字列長チェック
        if not(0 < len(user_id) <= 8) or not(0 < len(passward) <= 16):
            flash("パスワードかユーザIDの文字列の長さが不正です")
            return redirect('/login')
        
        #ログイン検証
        #login成功
        if( loginUI.loginUI(user_id,passward) ):
            session["user_id"] = user_id #セッションにユーザIDを登録
            session["is_login"] = True
            return redirect("/") #ログイン成功なら遷移
        #login失敗
        else: 
            flash('ユーザーIDとパスワードのどちらか、または両方が誤っています。')
            return redirect("/login") #もう一度ログイン画面へ

#M2.1 サインアップ画面への遷移処理
@app.route('/signup', methods = ("GET", "POST"))
def signup():
    
    if(request.method == "GET"):
        return signupUI.signupUI1()
    else:
        user_id = request.form.get("user_id")
        user_name = request.form.get("user_name")
        user_passward = request.form.get("user_passward")
        
        return signupUI.signupUI2(user_id,user_name,user_passward)    
#M3食事管理管理画面の遷移処理
@app.route('/', methods = ('GET', 'POST'))
def foodManagement():
    
    #ログイン検証
    if session["is_login"] != True:
        flash("ログインしてください。")
        return redirect("/login")
    
    
    #遷移
    return foodManagementUI.foodManagementUI()

#M3.5編集画面の遷移処理
@app.route('/edit')
def edit_mode():
    
    #ログイン検証
    if session["is_login"] != True:
        flash("ログインしてください。")
        return redirect("/login")
    
    #遷移
    return edit_modeUI.edit_modeUI()
        
    
#M4.1 食材追加画面への遷移処理
@app.route('/add')
def add():
    
    #ログイン検証
    if session["is_login"] != True:
        flash("ログインしてください。")
        return redirect("/login")
    
    #遷移
    return addFoodUI.addFoodUI()

#4.2削除処理への遷移処理
@app.route('/deleteIngredients', methods = ('GET','POST') )
def delete():
    if (request.method == 'POST'):
        #ログイン検証
        if session["is_login"] != True:
            flash("ログインしてください。")
            return redirect("/login")
    
        #遷移
        return deleteIngredientsUI.deleteIngredientsUI()
    

#M5.1 画像認証画面への遷移処理
@app.route('/imageReco')
def imageReco():
    #ログイン検証
    if session["is_login"] != True:
        flash("ログインしてください。")
        return redirect("/login")
    
    #遷移
    return imageRecognitionUI.imageRecognitionUI()

#M5.1.1 画像アップロードへの遷移処理
@app.route('/upload', methods = ('GET', 'POST'))
def upload():
    #ログイン検証
    if session["is_login"] != True:
        flash("ログインしてください。")
        return redirect("/login")
    
    #遷移
    return recoResultUI.recoResultUI()

#M5.2 通常の追加画面への遷移
@app.route('/add/normal/')
def addNormal():
    #ログイン検証
    if session["is_login"] != True:
        flash("ログインしてください。")
        return redirect("/login")
    
    #遷移
    return normalWayUI.normalWayUI()


#M6 通常追加確認画面への遷移処理
@app.route('/addResult', methods = ('GET', 'POST'))
def addResult():
    #ログイン検証
    if session["is_login"] != True:
        flash("ログアウトしてください。")
        return redirect("/login")
    
    #遷移
    return addResultUI.addResultUI()

#M7.1 レシピ検索食材選択画面への遷移処理
@app.route('/recipeSearch')
def recipeSearch():
    
    return recipeSearchUI.recipeSearchUI()

#M7.2 レシピ一覧画面への遷移処理
@app.route('/recipeList', methods = ('GET','POST'))
def recipeList():
    
    if(request.method == 'POST'):
        #ログイン検証
        if session["is_login"] != True:
            flash("ログインしてください。")
            return redirect("/login")
    
        #遷移
        #管理画面で選択された食材を取得
        ingredient_list = request.form.getlist('ingredients')
        print(ingredient_list)
        if (ingredient_list):
            return recipeListUI.recipeListUI(ingredient_list)
        
        else:
            return redirect("/recipeSearch")
        
        
#M8 レシピ詳細画面への遷移処理
@app.route('/recipeDetail/<uri>', methods = ('GET','POST'))
def recipeDetail(uri):
    #ログイン検証
    if session["is_login"] != True:
        flash("ログインしてください。")
        return redirect("/login")
    
    #遷移
    return recipeDetailUI.recipeDetailUI(uri)

    
        

#Flask実行
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
