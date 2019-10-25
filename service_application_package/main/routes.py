from flask import render_template, request, Blueprint
from service_application_package.main.forms import GenerationNumberAndStartForm
from service_application_package.main.universe import Universe
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import io
import base64
import pickle as pk

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
	def loadData(): 
		# for reading also binary mode is important 
		dbfile = open('vectorFiles', 'rb')      
		db = pk.load(dbfile) 
		for keys in db: 
		    print(keys, '=>', db[keys]) 
		dbfile.close() 
	#initialise universe
	u = Universe(GRID_SIZE, INITIAL_PREDATORS, INITIAL_PREYS)
	u.move_animals()

	return render_template('geneticModel.html', numberOfGenerations=form.numberOfGenerations, universe=1)
# def stop():
	# create stop function