from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, URL, Length

class MeetingImageForm(FlaskForm):
    meeting_id = IntegerField('Meeting ID', validators=[DataRequired()])
    url = StringField('Image URL', validators=[DataRequired(), URL(), Length(max=200)])
    caption = StringField('Caption', validators=[Length(max=100)])
