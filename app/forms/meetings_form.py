from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DateTimeField,
)
from wtforms.validators import (
    DataRequired,
    Length,
    URL,
    ValidationError,
)
from datetime import datetime


def date_check(form, field):
    date_time = str(field.data)

    dt = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
    if dt > datetime.utcnow():
        raise ValidationError("Date can't be set beyond present date.")


class MeetingForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=1, max=255)])
    meeting_date = DateTimeField(
        "Meeting Date",
        format="%Y-%m-%d %H:%M:%S",
        validators=[date_check, DataRequired()],
    )
    description = StringField("Description", validators=[DataRequired()])
    link = StringField("Link", validators=[DataRequired(), URL(), Length(max=255)])
