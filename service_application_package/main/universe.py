"""
implementation of the universe, which is everything living insde the predator  prey model
"""

from cell import Cell
from animals import Predator, Prey

import numpy.random as npr
import pickle as pk


class Universe():
    def __init__(self, SIZE, initial_pred_num, initial_prey_num):
        self.SIZE = SIZE
        self.cells = []
        self.predators = []
        self.preys = []
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
        #init predators
        for i in range(initial_pred_num):
            randomCell = self.cells[npr.randint(self.SIZE)][npr.randint(self.SIZE)]
            while not randomCell.contained_animal == None:
                randomCell = self.cells[npr.randint(self.SIZE)][npr.randint(self.SIZE)]
            self.predators.append(Predator(self, randomCell))
        #init preys
        for i in range(initial_prey_num):
            randomCell = self.cells[npr.randint(self.SIZE)][npr.randint(self.SIZE)]
            while not randomCell.contained_animal == None:
                randomCell = self.cells[npr.randint(self.SIZE)][npr.randint(self.SIZE)]
            self.preys.append(Prey(self, randomCell))
        

    def move_animals(self):
#        print len(self.predators), 'predators trying to move'
#        moved_predators = 0
#        for predator in self.predators:
#            if predator.already_moved:
#                print predator, 'already moved'
#                moved_predators +=1
#        print moved_predators, 'of them have alredy moved'
        for predator in self.predators:
            neighbouring_cells = predator.get_neighbouring_cells()
            neighbouring_preys = [cell for cell in neighbouring_cells if isinstance(cell.contained_animal, Prey)]
            neighbouring_empties = [cell for cell in neighbouring_cells if cell.contained_animal==None]
            if len(neighbouring_preys) == 1:
                predator.move_to_cell(neighbouring_preys[0])
            elif len(neighbouring_preys) > 1:
                randomNumber = npr.randint(len(neighbouring_preys))
                predator.move_to_cell(neighbouring_preys[randomNumber])
            elif len(neighbouring_empties) != 0:
                randomNumber = npr.randint(len(neighbouring_empties))
                predator.move_to_cell(neighbouring_empties[randomNumber])
            else:
                pass
                
        for prey in self.preys:
            neighbouring_cells = prey.get_neighbouring_cells()
            neighbouring_empties = [cell for cell in neighbouring_cells if cell.contained_animal==None]
            if len(neighbouring_empties) != 0:
                randomNumber = npr.randint(len(neighbouring_empties))
                prey.move_to_cell(neighbouring_empties[randomNumber])
            else:
                pass
            
            
    def apply_cheat_modifiers(self):
        if len(self.predators) < 5:
            for pred in self.predators:
                pred.MAX_HUNGER = 10000
        else:
            for pred in self.predators:
                pred.MAX_HUNGER = 6
            
            
    def prepare_next_round(self):
        for pred in self.predators:
            pred.already_moved = False
            pred.age +=1
            pred.not_eaten_since +=1
            pred.proliferated_since +=1
            pred.check_proliferation()
        for pred in self.predators:
            pred.check_death()
        for prey in self.preys:
            prey.already_moved = False
            prey.age +=1
            prey.proliferated_since +=1
            prey.check_proliferation()
        for prey in self.preys:
            prey.check_death()
            
        #this is the cheat to ensure that the equilibrium doesn't stop
        self.apply_cheat_modifiers()
        
        

    
    
    
    