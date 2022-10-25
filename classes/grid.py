from form import Form
class Grid:
    def __init__(self):
        self.__forms = []
    def getForms(self):
        return self.__forms
    def addForm(self, x, y, form):
        if(form.isForm()):
            self.__forms.append({'x':x, 'y':y, 'form':form})
    def create(self, forms):
        while True:
            print("\n\n\n0. Back")
            print("1. Add Form")
            choice = input("Enter your choice: ")
            if choice == '0':
                break
            elif choice == '1':
                x = input("\nEnter x: ")
                y = input("Enter y: ")
                choice_form = input("Enter form id: ")
                i=0
                while i < len(forms):
                    if i == choice_form:
                        self.addForm(x, y, forms[i])
                        break
                    i+=1
        