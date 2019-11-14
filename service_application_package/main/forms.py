from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
# from wtforms.validators import DataRequired
# from datetime import datetime

class GenerationNumberAndStartForm(FlaskForm):
    numberOfGenerations = IntegerField(default=100)
    numberOfPrey = IntegerField(default=15)
    amountOfGrass = IntegerField(default=100)
    amountOfPoison = IntegerField(default=5)
    mutationRate = IntegerField(default=0.5)
    start = SubmitField('Start Generating')