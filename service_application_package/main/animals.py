import numpy as np

class Animal:
	def __init__(self, genes, fitness, master, species, cell):
		self.genes = genes
		self.fitness = fitness
		self.MAX_AGE = 20
		self.MAX_HUNGER = 6
		self.PROLIFERATE_MIN_AGE = 10
		self.PROLIFERATE_MAX_AGE = 18
		self.PROLIFERATE_INTERVAL = 3
		self.master = master
		self.species = species
		self.cell = cell
		self.age = 0
		self.already_moved = False
		self.proliferated_since = 1000000
		cell.contained_animal = self
	def die(self):
	    self.cell.contained_animal = None
	    if self in self.master.elk:
	        self.master.elk.remove(self)
	    elif self in self.master.wolves:
	        self.master.wolves.remove(self)
            

	def check_proliferation(self):
		if self.age >= self.PROLIFERATE_MIN_AGE and self.age <= self.PROLIFERATE_MAX_AGE and self.proliferated_since > self.PROLIFERATE_INTERVAL:
			self.proliferate()

	def get_neighbouring_cells(self):
#        print 'getting neighbouring cells from x =', self.cell.x, 'y =', self.cell.y
		neighbouring_cells = []
		if self.cell.x > 0:
		    neighbouring_cells.append(self.master.cells[self.cell.x-1][self.cell.y])
		if self.cell.x < self.master.SIZE-1:
		    neighbouring_cells.append(self.master.cells[self.cell.x+1][self.cell.y])
		if self.cell.y > 0:
		    neighbouring_cells.append(self.master.cells[self.cell.x][self.cell.y-1])
		if self.cell.y < self.master.SIZE-1:
		    neighbouring_cells.append(self.master.cells[self.cell.x][self.cell.y+1])
		return neighbouring_cells