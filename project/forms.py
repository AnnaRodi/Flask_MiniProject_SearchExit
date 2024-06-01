from flask import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ChooseRoom(FlaskForm):
    destination = StringField("Destination: ", validators=[DataRequired()]) #выбор направления движения
    step_count = StringField("Step count: ", validators=[DataRequired()]) #выбор количества шагов
    is_monster = StringField("Is monster?: ", validators=[DataRequired()]) #выбор есть ли там монстр
    submit = SubmitField("Submit")