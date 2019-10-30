from __future__ import division
from flask import render_template, request, Blueprint
from service_application_package.main.forms import GenerationNumberAndStartForm
import argparse
from matplotlib import pyplot as plt
from pyp5 import *
import pickle
import json
import math
import numpy as np

ga = Blueprint('ga', __name__)

genes = []
lifeSpan = 500
@ga.route("/runGA/<int:numberOfGenerations>")
def start(numberOfGenerations):

    # create start def
    form = GenerationNumberAndStartForm()

    genes.append(np.random.rand(lifeSpan,2))
    # genes.append(np.linespace(-np.random.))
    head = Vector(1,1)
    return render_template('geneticModel.html', numberOfGenerations=form.numberOfGenerations, universe=head)