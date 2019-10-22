"""
runs the simulation and outputs the two populations on an animated matplotlib graph
"""

from universe import Universe

import matplotlib.pyplot as plt
import matplotlib.animation as animation


#input parameters
GRID_SIZE = 50
INITIAL_PREDATORS = 50
INITIAL_PREYS = 50

#initialise universe
u = Universe(GRID_SIZE, INITIAL_PREDATORS, INITIAL_PREYS)

#initialise graphics
fig = plt.figure('predator prey model')
ax = fig.add_subplot(111)
plot_x = []
plot_y1 = []
plot_y2 = []

def animate(i):
    u.move_animals()
    u.prepare_next_round()
    
    plot_x.append(i)
    plot_y1.append(len(u.predators))
    plot_y2.append(len(u.preys))
    
    ax.clear()
    ax.plot(plot_x, plot_y1, 'r', label='predators')
    ax.plot(plot_x, plot_y2, 'g', label='preys')
    ax.set_xlabel('time')
    ax.set_ylabel('population')
    ax.legend()
    
#run graphics 
ani = animation.FuncAnimation(fig, animate, interval=1)

