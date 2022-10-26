from hashlib import sha256
from guest import Guest
class User:
    def __init__(self, session):
        self.session = session
        self.__isAdm = False
        self.__name = ''
        self.__hash = ''
    #getandset methods from name, hash and session
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    def getHash(self):
        return self.__hash
    def getSession(self):
        return self.session
    def setSession(self, session):
        self.session = session
    def saltPassword(self, password):
        #encrypting password with sha256
        self.__hash = sha256(password.encode('utf-8')).hexdigest()
    def auth(self, password):
        hash = sha256(password.encode('utf-8')).hexdigest()
        if hash == self.__hash:
            return True
        else:
            return False
    def isAdm(self):
        return self.__isAdm