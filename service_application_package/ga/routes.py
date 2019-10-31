from __future__ import division
from flask import render_template, request, Blueprint
from service_application_package.main.forms import GenerationNumberAndStartForm
import argparse
from matplotlib import pyplot as plt
# from p5 import *
import pickle
import json
import math
import numpy as np
import random as r

ga = Blueprint('ga', __name__)

directions = [[-1,1],[0,1],[1,1],[-1,0],[0,0],[0,1],[-1,-1],[0,-1],[1,-1]]
genes = []
lifeSpan = 500
numberOfAgents = 200
sizeOfGrid = 1000
agents = []
@ga.route("/runGA/<int:numberOfGenerations>")
def start(numberOfGenerations):

    # create start def
    form = GenerationNumberAndStartForm()

    # genes.append(np.random.rand(lifeSpan,2))
    # genes.append(np.linespace(-np.random.))
    for a in range(len(numberOfAgents)):
    	agents.append(genes)
    for b in range(0,lifeSpan):
    	genes.append(r.choice(directions))
    return render_template('geneticModel.html', numberOfGenerations=form.numberOfGenerations, universe=genes)