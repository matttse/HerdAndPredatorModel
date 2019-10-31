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
import plotly.tools as tls
ga = Blueprint('ga', __name__)

directions = [[-1,1],[0,1],[1,1],[-1,0],[0,0],[0,1],[-1,-1],[0,-1],[1,-1]]
genes = []
lifeSpan = 500
numberOfAgents = 200
sizeOfGrid = 1000
agents = []
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
    return render_template('geneticModel.html', numberOfGenerations=form.numberOfGenerations, universe=len(agents))
    
@ga.route("/other", methods=['GET','POST'])
def other():
	# tls.get_embed('https://plot.ly/~chris/1638')
    gapminder = px.data.gapminder()
    fig = px.scatter(gapminder, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
               size="pop", color="continent", hover_name="country",
               log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
    return render_template('animation.html', show=fig.show())