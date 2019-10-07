from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
# from wtforms.validators import DataRequired
# from datetime import datetime

class GenerationNumberAndStartForm(FlaskForm):
    numberOfGenerations = IntegerField(default=100)
    start = SubmitField('Start Generating')