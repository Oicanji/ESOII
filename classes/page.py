from grid import Grid
class Page:
    def __init__(self):
        self.__grids = []
        self.__gridCount = 0
    def addGrid(self, grid, x, y):
        self.__gridCount+=1
        self.__grids.append({'id':self.__gridCount,'x':x, 'y':y,'grid': grid})
    def getGrid(self, id):
        for grid in self.__grids:
            if(grid['id'] == id):
                return grid
        return None
    def removeGrid(self, id):
        for grid in self.__grids:
            if(grid['id'] == id):
                self.__grids.remove(grid)
                return True
        return False
    def getGrids(self):
        return self.__grids
    
    def create(self, grids):
        while True:
            print("\n\n\n0. Back")
            print("1. Add Grid")
            print("2. Remove Grid")
            choice = input("Enter your choice: ")
            if choice == '0':
                break
            elif choice == '1':
                x = input("\nEnter x: ")
                y = input("Enter y: ")
                choice_grid = input("Enter grid id: ")
                i=0
                while i < len(grids):
                    if i == choice_grid:
                        self.addGrid(grids[i], x, y)
                        break
                    i+=1
            elif choice == '2':
                choice_grid = input("Enter grid id: ")
                self.removeGrid(choice_grid)