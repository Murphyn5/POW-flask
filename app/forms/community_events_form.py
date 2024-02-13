from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, URL


class CommunityEventForm(FlaskForm):
    days = StringField("Days", validators=[Length(max=255)])
    dates = StringField("Dates", validators=[Length(max=255)])
    times = StringField("Times", validators=[Length(max=255)])
    location = StringField("Location", validators=[DataRequired(), Length(max=255)])
    title = StringField("Title", validators=[DataRequired(), Length(max=255)])
    description = TextAreaField(
        "Description", validators=[DataRequired(), Length(max=1000)]
    )
    link = StringField("Link", validators=[URL(), Length(max=255)])
