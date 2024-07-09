from searchPass import searchPass

def userAuthentication(userID, passward):
    passResult = False
    
    correctPass = searchPass(userID)
    print(correctPass,userID)
    
    if passward == correctPass:
        
        passResult = True
        
    return passResult