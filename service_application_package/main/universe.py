"""
implementation of the universe, which is everything living insde the predator  prey model
"""

from service_application_package.main.cell import Cell
from service_application_package.main.elk import Elk
from service_application_package.main.wolf import Wolf

import numpy.random as npr
import pickle as pk


class Universe():
    def __init__(self, SIZE, initial_pred_num, initial_prey_num):
        self.SIZE = SIZE
        self.cells = []
        self.wolves = []
        self.elk = []
        self.init_cells_and_animals(initial_pred_num, initial_prey_num)
        
    def save_pkl(self): #just for testing purposes, nothing sensible
        f = open('testpickle.pk', 'wb')
        pk.dump(self, f, protocol=0)
        f.close()
        
        
    def init_cells_and_animals(self, initial_pred_num, initial_prey_num):
        #init cells
        for x in range(self.SIZE):
            self.cells.append([])
            for y in range(self.SIZE):
                self.cells[-1].append(Cell(x, y))
        #init wolves
        for i in range(initial_pred_num):
            randomCell = self.cells[npr.randint(self.SIZE)][npr.randint(self.SIZE)]
            while not randomCell.contained_animal == None:
                randomCell = self.cells[npr.randint(self.SIZE)][npr.randint(self.SIZE)]
            self.wolves.append(Wolf(self, randomCell))
        #init elk
        for i in range(initial_prey_num):
            randomCell = self.cells[npr.randint(self.SIZE)][npr.randint(self.SIZE)]
            while not randomCell.contained_animal == None:
                randomCell = self.cells[npr.randint(self.SIZE)][npr.randint(self.SIZE)]
            self.elk.append(Elk(self, randomCell))
        

    def move_animals(self):
        for wolf in self.wolves:
            neighbouring_cells = wolf.get_neighbouring_cells()
            neighbouring_elk = [cell for cell in neighbouring_cells if isinstance(cell.contained_animal, Elk)]
            neighbouring_empties = [cell for cell in neighbouring_cells if cell.contained_animal==None]
            if len(neighbouring_elk) == 1:
                x=wolf.move_to_cell(neighbouring_elk[0])
            elif len(neighbouring_elk) > 1:
                randomNumber = npr.randint(len(neighbouring_elk))
                x=wolf.move_to_cell(neighbouring_elk[randomNumber])
            elif len(neighbouring_empties) != 0:
                randomNumber = npr.randint(len(neighbouring_empties))
                x=wolf.move_to_cell(neighbouring_empties[randomNumber])
            else:
                pass
            return x 
                
        # for elk in self.elks:
        #     neighbouring_cells = elk.get_neighbouring_cells()
        #     neighbouring_empties = [cell for cell in neighbouring_cells if cell.contained_animal==None]
        #     if len(neighbouring_empties) != 0:
        #         randomNumber = npr.randint(len(neighbouring_empties))
        #         elk.move_to_cell(neighbouring_empties[randomNumber])
        #     else:
        #         pass
            
            
    def apply_cheat_modifiers(self):
        if len(self.wolves) < 5:
            for pred in self.wolves:
                pred.MAX_HUNGER = 10000
        else:
            for pred in self.wolves:
                pred.MAX_HUNGER = 6
            
            
    def prepare_next_round(self):
        for pred in self.wolves:
            pred.already_moved = False
            pred.age +=1
            pred.not_eaten_since +=1
            pred.proliferated_since +=1
            pred.check_proliferation()
        for pred in self.wolves:
            pred.check_death()
        for prey in self.elk:
            prey.already_moved = False
            prey.age +=1
            prey.proliferated_since +=1
            prey.check_proliferation()
        for prey in self.elk:
            prey.check_death()
            
        #this is the cheat to ensure that the equilibrium doesn't stop
        self.apply_cheat_modifiers()
        
        

    
    
    
    