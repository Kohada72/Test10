from userAuthentication import userAuthentication

'''-------------------------------------------------------------------- 
Function Name       : loginUI
Designer            : 人見淳史
Date                : 2024.05.29
Function            : W1 ログイン画面を表示する
Argument            : なし
Return              : login_result
----------------------------------------------------------------------'''
#ログイン画面表示処理
def loginUI(userID, passward):
    
    login_result = False
    
    if userAuthentication(userID,passward):
        login_result = True
    else:
        login_result = False
    
    return login_result