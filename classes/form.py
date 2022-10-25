class Form:
    def __init__(self):
        self.__border_width = 1
        self.__border_style = 'solid'
        self.__border_color = 'black'
    def setBorder(self, width, style, color):
        self.__border_width = width
        self.__border_style = style
        self.__border_color = color
    def getBorder(self):
        return [self.__border_width, self.__border_style, self.__border_color]
    def setImage(self, image):
        self.__image = image
    def getImage(self):
        return self.__image
    def addPoint(self, x, y):
        self.__x.append(x)
        self.__y.append(y)
        
    def isForm(self):
        if(len(self.__x) > 2 and len(self.__y) > 2):
            return True
        return False
