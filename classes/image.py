class Image:
    __url = ''
    def __init__(self, url):
        self.__url = url
    def get(self):
        return self.__url