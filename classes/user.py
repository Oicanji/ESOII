from hashlib import scrypt
from guest import Guest
class User:
    def __init__(self, session):
        self.session = session
    #getandset methods from name, hash and session
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    def getHash(self):
        return self.__hash
    def setHash(self, hash):
        self.__hash = hash
    def getSession(self):
        return self.__session
    def setSession(self, session):
        self.__session = session
        
    def saltPassword(password):
        #use pycryptodome to salt 'cavalodefogo' in password
        salt = b'$2b$12$' + b'cavalodefogo'
        #use pycryptodome to hash the salted password
        hash = scrypt.hash(password, salt, N=2**14, r=8, p=1, buflen=32)
        return hash
    def createUser(self, name, hash):
        self.__name = name
        self.__hash = hash
        self.__isAdm = False
    def auth(self, password):
        #use pycryptodome to salt 'cavalodefogo' in password
        salt = b'$2b$12$' + b'cavalodefogo'
        #use pycryptodome to hash the salted password
        hash = scrypt.hash(password, salt, N=2**14, r=8, p=1, buflen=32)
        if hash == self.__hash:
            return True
        else:
            return False
    def isAdm(self):
        return self.__isAdm
    