from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, URL, Length


class DocumentaryForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=255)])
    source = StringField("Source", validators=[DataRequired(), Length(max=255)])
    description = TextAreaField(
        "Description", validators=[DataRequired(), Length(max=1000)]
    )
    link = StringField("Link", validators=[DataRequired(), URL(), Length(max=255)])
