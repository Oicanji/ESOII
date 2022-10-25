from this import d
from image import Image
class ImageGalerie:
    __id = 0
    __name = ''
    __owner_id = 0
    __list_image = []
    def __init_(self, id, name, owner_id):
        self.__id = id
        self.__name = name
        self.__owner_id = owner_id
    #get ans set methods from id name and owner_id
    def getId(self):
        return self.__id
    def setId(self, id):
        self.__id = id
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    def getOwnerId(self):
        return self.__owner_id
    def setOwnerId(self, owner_id):
        self.__owner_id = owner_id
    
    def addImage(self, image):
        self.__list_image.append(image)
    def getListImage(self):
        return self.__list_image
    