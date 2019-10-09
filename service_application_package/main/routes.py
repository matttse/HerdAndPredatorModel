from flask import render_template, request, Blueprint
# from wtforms import IntegerField
from service_application_package.main.forms import GenerationNumberAndStartForm

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
	
	form = GenerationNumberAndStartForm()
	# return render_template('home.html')
	return render_template('home.html', nog=form.numberOfGenerations)
@main.route("/geneticModel/<int:numberOfGenerations>")
def start(numberOfGenerations):
	form = GenerationNumberAndStartForm()
	return render_template('geneticModel.html', numberOfGenerations=form.numberOfGenerations, form=form)
# def stop():
	# create stop function