'''----------------------------------------------------------------- 
File Name		: searchPass.py
Version		: V1.0 
Designer		: 上之山 将太
Date			: 2024.07.05
Purpose       	: ユーザ認証でのパスワードの参照
--------------------------------------------------------------------'''

from db_operation import getUser


'''-------------------------------------------------------------------- 
Function Name       : searchPass
Designer            : 上之山 将太
Date                : 2024.07.05
Function            : 引数のidに該当するユーザのパスワードを渡す
Argument            : id
Return              : user_info["password"] (str)
----------------------------------------------------------------------'''

def searchPass(id):
    user_info = getUser(id)
    if user_info and "password" in user_info:
        return user_info["password"]
    else:
        return ""
    
#print(validateUserInfo(22))
#print(type(validateUserInfo(22)))
