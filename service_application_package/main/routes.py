from flask import render_template, request, Blueprint
from service_application_package.main.forms import GenerationNumberAndStartForm
from service_application_package.main.animals import Animal
from service_application_package.main.elk import Elk
from service_application_package.main.wolf import Wolf
from service_application_package.main.cell import Cell
from service_application_package.main.universe import Universe
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import io
import base64

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/geneticModel/<int:numberOfGenerations>")
def home(numberOfGenerations):
	
	form = GenerationNumberAndStartForm()

	return render_template('home.html', numberOfGenerations=form.numberOfGenerations, form=form)
@main.route("/start")
def start():
	# create start function
	form = GenerationNumberAndStartForm()
	# img = io.BytesIO()

	# y = [1,2,3,4,5]
	# x = [0,2,1,3,4]

	# plt.plot(x,y)
	# plt.savefig(img, format='png')
	# img.seek(0)

	# plot_url = base64.b64encode(img.getvalue()).decode()
	# return '<img src="data:image/png;base64,{}">'.format(plot_url)
	#input parameters
	GRID_SIZE = 50
	INITIAL_PREDATORS = 50
	INITIAL_PREYS = 50

	#initialise universe
	u = Universe(GRID_SIZE, INITIAL_PREDATORS, INITIAL_PREYS)

	return render_template('geneticModel.html', numberOfGenerations=form.numberOfGenerations, universe=u.move_animals())
# def stop():
	# create stop function