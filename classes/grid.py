from form import Form
class Grid:
    def __init__(self, id):
        self.__id = id
        self.__forms = []
    def getId(self):
        return self.__id
    def setId(self, id):
        self.__id = id
    def getForms(self):
        return self.__forms
    def addForm(self, x, y, form):
        if(form.isForm()):
            self.__forms.append({'x':x, 'y':y, 'form':form})