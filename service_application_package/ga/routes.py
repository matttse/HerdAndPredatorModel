from flask import render_template, request, Blueprint
from service_application_package.main.forms import GenerationNumberAndStartForm
import argparse
from service_application_package.ga.grid import Grid
from matplotlib import pyplot as plt
# from p5 import *
import pickle
import json
import math
import numpy as np
import random as r
import plotly.express as px
import plotly.graph_objects as go
import plotly.tools as tls
ga = Blueprint('ga', __name__)
iris = px.data.iris()
fig = px.scatter(iris, x="sepal_width",y="sepal_length",color="species")
directions = [[-1,1],[0,1],[1,1],[-1,0],[0,0],[0,1],[-1,-1],[0,-1],[1,-1]]
genes = []
lifeSpan = 500
numberOfAgents = 200
sizeOfGrid = 50
agentList = []
agents = []
agentPosition = []
# @ga.route("/runGA/<int:numberOfGenerations>")
# def start(numberOfGenerations):
@ga.route("/geneticModel", methods=['GET','POST'])
def start():
    # create start def
    form = GenerationNumberAndStartForm()

    # # genes.append(np.random.rand(lifeSpan,2))
    # # genes.append(np.linespace(-np.random.))
    for a in range(0,numberOfAgents):
    	agents.append(genes)
    for b in range(0,lifeSpan):
    	genes.append(r.choice(directions))
    # Grid.draw()
    return render_template('geneticModel.html',
        numberOfGenerations=form.numberOfGenerations,
        numberOfPrey=form.numberOfPrey,
        amountOfGrass=form.amountOfGrass,
        amountOfPoison=form.amountOfPoison,
        mutationRate=form.mutationRate
        )
    
@ga.route("/other", methods=['GET','POST'])
def other():
    # gapminder = px.data.gapminder()
    # fig = px.scatter(gapminder, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
    #            size="pop", color="continent", hover_name="country",
    #            log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
    for a in range(0,numberOfAgents):
    	agents.append(genes)# list of vectors taken for each agent
	    
	    # agentPosition.append(np.random.randint(0,high=sizeOfGrid,size=2))#append starting positions to list of positions
    for b in range(0,lifeSpan):
    	genes.append(r.choice(directions))
    # for c in range(len(agentPosition)):
    # 	agentList.append(agentPosition[c])
    p1 = np.random.randint(0,high=sizeOfGrid,size=2)
    p2 = p1 - agents[1][1]
    # fig = go.Figure(
    # 	data=[go.Scatter(x=[0,1], y=[0,1])],
    # 	layout=go.Layout(
    # 		xaxis=dict(range=[0,sizeOfGrid],autorange=False),
    # 		yaxis=dict(range=[0,sizeOfGrid],autorange=False),
    # 		title="Prey Predator Model",
    # 		updatemenus=[dict(
    # 			type="buttons",
    # 			buttons=[dict(label="Play",
    # 					method="animate",
    # 					args=[None])])]
    # 	),
    # 	frames=[go.Frame(data=[go.Scatter(x=[1,2],y=[1,2])]),
    # 			go.Frame(data=[go.Scatter(x=[1,4],y=[1,4])]),
    # 			go.Frame(data=[go.Scatter(x=[3,4],y=[3,4])],
    # 				layout=go.Layout(title_text="Completed"))]

    # 	)
    	# frames=[go.Frame(data=[go.Scatter(x=[p1[0],p1[1]],y=[p1[0],p1[1]])]),
    	# 		go.Frame(data=[go.Scatter(x=[p2[0],p2[1]],y=[p2[0],p2[1]])]),
    	# 		go.Frame(data=[go.Scatter(x=[3,4],y=[3,4])],
    	# 			layout=go.Layout(title_text="Completed"))]
    # fig = go.Figure(
    # 	data=[go.Scatter(x=[0,1], y=[0,1])],
    # 	layout=go.Layout(
    # 		xaxis=dict(range=[0,50],autorange=False),
    # 		yaxis=dict(range=[0,50],autorange=False),
    # 		title="Prey Predator Model",
    # 		updatemenus=[dict(
    # 			type="buttons",
    # 			buttons=[dict(label="Play",
    # 					method="animate",
    # 					args=[None])])]
    # 	),
    # 	frames=[go.Frame(data=[go.Scatter(
    # 		x=[genes[k]],
    # 		y=[genes[k]],
    # 		mode="markers",
    # 		marker=dict(color="red", size=10))])
    # 			for k in range(len(genes))]
    # 	)
    # p1 = np.random.randint(0,high=sizeOfGrid,size=2)
    # p2 = p1 - agents[1][1]
	# fig = go.Figure(
 #    	data=[go.Scatter(x=[0,1], y=[0,1])],
 #    	layout=go.Layout(
 #    		xaxis=dict(range=[0,50],autorange=False),
 #    		yaxis=dict(range=[0,50],autorange=False),
 #    		title="Prey Predator Model",
 #    		updatemenus=[dict(
 #    			type="buttons",
 #    			buttons=[dict(label="Play",
 #    					method="animate",
 #    					args=[None])])]
 #    	),
 #    	frames=[go.Frame(data=[go.Scatter(
 #    		x=[agents[k]],
 #    		y=[agents[k]],
 #    		mode="markers",
 #    		marker=dict(color="red", size=10))])
 #    			for k in range(len(agents))]
 #    	)
 	
    return render_template('animation.html', xvector=agents[1][1],show=fig.show(),position=p1,position2=p2)
	