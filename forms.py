from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length


class AddPetForm(FlaskForm):

    name = StringField("Enter Pet Name", validators=[InputRequired()])
    species = SelectField("Enter Pet Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Enter Pet Photo", validators=[URL(), Optional()])
    age = IntegerField("Enter Pet Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Add Notes", validators=[Optional(), Length(min=10)])

class EditPetForm(FlaskForm):

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")

