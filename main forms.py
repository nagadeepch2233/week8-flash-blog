from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    query = StringField(
        "Search",
        validators=[DataRequired(), Length(min=2)]
    )
    submit = SubmitField("Search")
