"""
generates a gui, from where you can choose the type of output and set the initial numbers of animals
nice but sometimes has problems with different screen sizes
"""

from universe import Universe

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pygame
import os
import tkinter as tk

root = tk.Tk(className='predator prey model')
root.geometry('300x170')
frame = tk.Frame(root)
frame.pack()

gridSize = tk.IntVar()
gridSize.set(50)
initialPred = tk.IntVar()
initialPred.set(100)
initialPrey = tk.IntVar()
initialPrey.set(50)
outputForm = tk.StringVar()
outputForm.set('animation')
want_to_run = False

def runner():
    global grid_size, initial_pred, initial_prey, output_form, want_to_run
    grid_size = gridSize.get()
    initial_pred = initialPred.get()
    initial_prey = initialPrey.get()
    output_form = outputForm.get()
    root.destroy()
    want_to_run = True
    
def helper():
    os.startfile('helper.txt')

label1 = tk.Label(frame, text='Grid size:')
label1.grid(row=1, column=1)
gridSizeEntry = tk.Entry(frame, textvariable=gridSize, width=7)
gridSizeEntry.grid(row=1, column=2)
label2 = tk.Label(frame, text='Initial number of predators:')
label2.grid(row=2, column=1)
initialPredEntry = tk.Entry(frame, textvariable=initialPred, width=7)
initialPredEntry.grid(row=2, column=2)
label3 = tk.Label(frame, text='Initial number of preys:')
label3.grid(row=3, column=1)
initialPreyEntry = tk.Entry(frame, textvariable=initialPrey, width=7)
initialPreyEntry.grid(row=3, column=2)
label4 = tk.Label(frame, text='Choose output form:')
label4.grid(row=4, column=1)
outputFormMenu = tk.OptionMenu(frame, outputForm, 'animation', 'plot', 'both (very slow)')
outputFormMenu.grid(row=4, column=2)
runButton = tk.Button(frame, text='RUN!', command=runner, bg='orange', width=6, height=2)
runButton.grid(row=5, column=2)
helperButton = tk.Button(frame, text='HELP', command=helper, bg='orange', width=6, height=2)
helperButton.grid(row=5, column=1)

root.mainloop()


if want_to_run:
    
    if output_form == 'animation':
        DISPLAY_SIZE = 500
        ROUNDS_PER_SEC = 100
        #initialise universe
        u = Universe(grid_size, initial_pred, initial_prey)
        TILE_SIZE = DISPLAY_SIZE / grid_size
        
        #initialise pygame
        pygame.init()
        screen = pygame.display.set_mode((DISPLAY_SIZE, DISPLAY_SIZE))
        pygame.display.set_caption('Predator prey model')
        clock = pygame.time.Clock()
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        
        #main pygame loop
        want_to_run = True
        while want_to_run:
            #EVENT HANDLING
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    want_to_run = False
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x:
                        want_to_run = False
                        
            #GAME LOGIC
            u.move_animals()
            u.prepare_next_round()
            
            #GRAPHICS
            screen.fill(BLACK)
            for predator in u.predators:
                pygame.draw.rect(screen, RED, (predator.cell.x*TILE_SIZE, predator.cell.y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            for prey in u.preys:
                pygame.draw.rect(screen, GREEN, (prey.cell.x*TILE_SIZE, prey.cell.y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            
            pygame.display.flip()
            clock.tick(ROUNDS_PER_SEC)
            
        pygame.quit()
        u.save_pkl() #just for testing purposes, nothing sensible
        
        
        
    elif output_form == 'plot':
        #initialise universe
        u = Universe(grid_size, initial_pred, initial_prey)
        
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
    
        
    
    elif output_form == 'both (very slow)':        
        #initialise universe
        u = Universe(grid_size, initial_pred, initial_prey)
        
        #initialise graphics
        fig = plt.figure('predator prey model', figsize=(10,10))
        ax1 = fig.add_subplot(2 ,1, 1)
        ax2 = fig.add_subplot(2, 1, 2)
        plot1_x = []
        plot1_y1 = []
        plot1_y2 = []
        
        def animate(i):
            u.move_animals()
            u.prepare_next_round()
            
            #plot 1 comes
            plot1_x.append(i)
            plot1_y1.append(len(u.predators))
            plot1_y2.append(len(u.preys))
            
            ax1.clear()
            ax1.plot(plot1_x, plot1_y1, 'r', label='predators')
            ax1.plot(plot1_x, plot1_y2, 'g', label='preys')
            ax1.legend()
            
            #plot 2 comes
            ax2.clear()
            ax2.axis([0, grid_size, 0, grid_size])
            for pred in u.predators:
                ax2.add_artist(plt.Rectangle((pred.cell.x, pred.cell.y), 1, 1, fc='r'))
            for prey in u.preys:
                ax2.add_artist(plt.Rectangle((prey.cell.x, prey.cell.y), 1, 1, fc='g'))
            
        #run graphics 
        ani = animation.FuncAnimation(fig, animate, interval=1)
        
        
        
    else:
        raise Exception('output_form was not recognised!')


