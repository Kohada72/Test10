'''-------------------------------------------------------------------- 
Function Name       : userAuthentication
Designer            : 人見　淳史
Date                : 2024.07.12
Function            : 入力されたユーザIDとそのパスワードが正当かどうかを返す
Argument            : なし
Return              : bool passResult
----------------------------------------------------------------------'''
from searchPass import searchPass

def userAuthentication(userID, passward):
    passResult = False
    
    correctPass = searchPass(userID)
    print(correctPass,userID)
    
    if passward == correctPass:
        
        passResult = True
        
    return passResult