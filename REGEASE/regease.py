import re

#emailRe stands for email regex
emailRe=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def emailVd(email):
    if(re.match(emailRe, email)):
        return True
 
    else:
        return False


#for difficult password
def passwordVd(password):
      
    SpecialSym =['@', '#', '$', '%','&',')','(','+','-','*']

    if len(password) < 8:
        return False
          
    if len(password) > 20:
        return False
          
    if not any(char.isdigit() for char in password):
        return False
          
    if not any(char.isupper() for char in password):
        return False
          
    if not any(char.islower() for char in password):
       return False
          
    if not any(char in SpecialSym for char in password):
        return False
    else:
        return True
 
 
#for an appropriate username with no special characters
usernameRe=r'^[a-zA-Z0-9]{6,12}$' #max 12 characters 
def usernameVd(username):
    if(len(username)<6):
        return False       #length should be minimum 6 characters
    elif(re.match(usernameRe,username)):
        return True
    else:
        return False
 
 
if __name__ == '__main__':
 
    emailVd(email="")
    passwordVd(password="")
    usernameVd(username="")