from service_application_package.main.animals import Animal
import numpy.random as npr

class Wolf(Animal):
    def __init__(self, master, cell):
        Animal.__init__(self, master, 'predator', cell)
        self.not_eaten_since = 0
#        self.PROLIFERATE_INTERVAL = 5
        
        
    def move_to_cell(self, new_cell):
        if not self.already_moved:
            self.cell.contained_animal = None
            self.cell = new_cell
            if isinstance(self.cell.contained_animal, Prey):
                self.eat(self.cell.contained_animal)
            else:
                pass
            self.already_moved = True
            self.cell.contained_animal = self
        else:
#            print 'predator tried to move twice!'
            raise Exception('predator tried to move twice!')
            

    def proliferate(self):
        neighbours = [cell for cell in self.get_neighbouring_cells() if cell.contained_animal == None]
        if len(neighbours) != 0:
            kid_cell = npr.choice(neighbours)
            self.master.predators.append(Wolf(self.master, kid_cell))
            self.proliferated_since = 0
#            print 'predator proliferated'
#        else:
#            print 'predator couldn\'t proliferate'
            
            
    def check_death(self):
        if self.age > self.MAX_AGE:
            self.die()
#            print 'predator died'
        if self.not_eaten_since > self.MAX_HUNGER:
#            print 'dying:', self
            self.die()
#            print 'predator died from hunger'
                
                
    def eat(self, prey):
#        print 'predator ate'
        self.not_eaten_since = 0
        prey.die()