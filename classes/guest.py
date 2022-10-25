import random
import string
class Guest:
    def __init__(self):
        self.__session = self.createToken()
    def getSession(self):
        return self.__session
    def createToken(self):
        #generate a random token with numbers ans letters with 32 characters
        token = ''
        for i in range(32):
            token += random.choice(string.ascii_letters + string.digits)
        self.__session['token'] = token
        return token
    def login(self, login):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        for i in login:
            if i.getName() == name:
                if i.auth(password):
                    print("Login successful")
                    return i
                else:
                    print("Login failed")
                    return False