from matplotlib import pyplot as plt

class Grid:

    def __init__(self, xDim, yDim)
    	self.grid = [[[] for x in range(xDim)] for y in range(yDim)]
    	self.agentList = []
    # print (grid)
	def draw(self):
	    plt.clf()
	    xs = [[], [], []]
	    ys = [[], [], []]
	    # for agents in self.agentList:
	    #     x = agents[1]
	    #     y = agents[2]
	    #     type = agents[3]
	    #     if type == 0:
	    #         xs[0].append(x)
	    #         ys[0].append(y)
	    #     elif type == 1:
	    #         xs[1].append(x)
	    #         ys[1].append(y)
	    #     else:
	    #         xs[2].append(x)
	    #         ys[2].append(y)
	    # xys = [xs[0],ys[0]]
	    

	    # plt.scatter(xs[2], ys[2], color='g')
	    # plt.scatter(xs[1], ys[1], color='b')
	    # plt.scatter(xs[0], ys[0], color='r')
	    plt.axis([-1, self.xDim, -1, self.yDim])
	    # fig = plt.figure()
	    # pickle.dump(fig, open('FO','wb'))
	    # plt.pause(0.01)
	    # plt.draw()