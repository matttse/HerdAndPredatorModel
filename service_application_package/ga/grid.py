

class Grid:

    def __init__(self, xDim, yDim, agent):
    	self.grid = [[[] for x in range(xDim)] for y in range(yDim)]
    	self.agentList = []
    	
    # print (grid)
