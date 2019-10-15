class DNA():
	def __init__(self, genes, fitness, behavior, strategy):
		self.Genes = genes
		self.Fitness = fitness
		self.Behavior = behavior
		self.Strategy = strategy
    def __len__(self) :
        return len(self.genes)
    
    def reset(self) :
        self.fitness = float('-inf')

class Strategies(Enum):
    Create = 0,
    Mutate = 1,
    Crossover = 2