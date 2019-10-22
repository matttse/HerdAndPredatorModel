"""
these cells keep track of which position are occupied and which are unoccupied by animals
"""


class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.contained_animal = None
        
        
    def show(self):
        print(('x =', self.x))
        print(('y =', self.y))