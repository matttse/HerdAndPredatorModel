from service_application_package.main.animal import Animal
import numpy.random as npr

class Elk(Animal):
    def __init__(self, master, cell):
        Animal.__init__(self, master, 'prey', cell)
#        self.PROLIFERATE_INTERVAL = 3
        
        
    def move_to_cell(self, new_cell):
        if not self.already_moved:
            self.cell.contained_animal = None
            self.cell = new_cell
            self.already_moved = True
            self.cell.contained_animal = self
        else:
#            print 'prey tried to move twice!'
            raise Exception('prey tried to move twice!')
            
            
    def proliferate(self):
        neighbours = [cell for cell in self.get_neighbouring_cells() if cell.contained_animal == None]
        if len(neighbours) != 0:
            kid_cell = npr.choice(neighbours)
            self.master.preys.append(Prey(self.master, kid_cell))
            self.proliferated_since = 0
#            print 'prey proliferated'
#        else:
#            print 'prey couldn\'t proliferate'
        
            
    def check_death(self):
        if self.age > self.MAX_AGE:
            self.die()
#            print 'prey died'

        