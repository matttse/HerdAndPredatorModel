from flask import render_template, request, Blueprint
from service_application_package.main.forms import GenerationNumberAndStartForm
import argparse
from matplotlib import pyplot as plt
import pyp5js
import pickle
import json
ga = Blueprint('ga', __name__)

##Rocket Object
def Rocket(dna):
	if dna
@ga.route("/runGA/<int:numberOfGenerations>")
def start():

	# create start def
	form = GenerationNumberAndStartForm()


	return render_template('geneticModel.html', numberOfGenerations=form.numberOfGenerations, universe=array)



# def stop():
	# create stop def