from flask import render_template, request, Blueprint
# from wtforms import IntegerField
from service_application_package.main.forms import GenerationNumberAndStartForm

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
	
	form = GenerationNumberAndStartForm()
	return render_template('home.html')
	# return render_template('home.html', form.numberOfGenerations)
# def start():
	# form = GenerationNumberAndStartForm()
	# create start function
# def stop():
	# create stop function