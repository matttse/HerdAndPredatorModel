from flask import render_template, request, Blueprint
from service_application_package.main.forms import GenerationNumberAndStartForm

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

	return render_template('geneticModel.html', numberOfGenerations=form.numberOfGenerations)
# def stop():
	# create stop function