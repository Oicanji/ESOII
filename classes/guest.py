import random
import string
class Guest:
    def __init__(self):
        self.__session = ''
        self.createToken()
    def getSession(self):
        return str(self.__session)
    def createToken(self):
        self.__session = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
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