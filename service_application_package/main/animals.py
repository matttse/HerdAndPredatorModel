import numpy as np
from pyp5js import *
class DNA():
	def __init__(self):
		if hasattr(self.genes):
			self.genes = genes
		else:
			self.genes = []
			for gene in genes:
				# genes.append(np.random(3,4))
				genes.append(p5.Vector.random2D())
	def mating(mate):
		childDNA = []
		midPoint = floor(random(self.genes.length))

		for i in range(len(genes)):
			if (i > midPoint):
				childDNA[i] = self.genes[i]
			else:
				childDNA[i] = mate.genes[i]
		return self


class Animal(DNA):
	# def __init__(self, genes, fitness, master, species, cell):
	def __init__(self, dna):
		DNA.__init__(self.dna, dna)
		self.fitness = 0
		self.border = False
		self.collision = False
		self.velocity = createVector()
		self.acceleration = createVector()
		# self.MAX_AGE = 20
		# self.MAX_HUNGER = 6
		# self.PROLIFERATE_MIN_AGE = 10
		# self.PROLIFERATE_MAX_AGE = 18
		# self.PROLIFERATE_INTERVAL = 3
		# self.master = master
		# self.species = species
		# self.cell = cell
		# self.age = 0
		# self.already_moved = False
		# self.proliferated_since = 1000000
		# cell.contained_animal = self
	# def die(self):
	#     self.cell.contained_animal = None
	#     if self in self.master.elk:
	#         self.master.elk.remove(self)
	#     elif self in self.master.wolves:
	#         self.master.wolves.remove(self)
            

# 	def check_proliferation(self):
# 		if self.age >= self.PROLIFERATE_MIN_AGE and self.age <= self.PROLIFERATE_MAX_AGE and self.proliferated_since > self.PROLIFERATE_INTERVAL:
# 			self.proliferate()

# 	def get_neighbouring_cells(self):
# #        print 'getting neighbouring cells from x =', self.cell.x, 'y =', self.cell.y
# 		neighbouring_cells = []
# 		if self.cell.x > 0:
# 		    neighbouring_cells.append(self.master.cells[self.cell.x-1][self.cell.y])
# 		if self.cell.x < self.master.SIZE-1:
# 		    neighbouring_cells.append(self.master.cells[self.cell.x+1][self.cell.y])
# 		if self.cell.y > 0:
# 		    neighbouring_cells.append(self.master.cells[self.cell.x][self.cell.y-1])
# 		if self.cell.y < self.master.SIZE-1:
# 		    neighbouring_cells.append(self.master.cells[self.cell.x][self.cell.y+1])
# 		return neighbouring_cells
