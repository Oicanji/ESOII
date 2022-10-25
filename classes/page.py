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