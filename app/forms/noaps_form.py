from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField
from wtforms.validators import DataRequired, URL, Length


class NoapForm(FlaskForm):
    operation_name = StringField(
        "Operation Name", validators=[DataRequired(), Length(min=1, max=255)]
    )
    noap_id = StringField(
        "NOAP ID", validators=[DataRequired(), Length(min=1, max=255)]
    )
    report_filed = DateTimeField("Report Filed", validators=[DataRequired()])
    fully_implemented_written_plan = DateTimeField("Fully Implemented Written Plan")
    start_date = DateTimeField("Start Date")
    end_date = DateTimeField("End Date")
    permit_link = StringField(
        "Permit Link", validators=[DataRequired(), URL(), Length(max=255)]
    )
    ferns_link = StringField(
        "Ferns Link", validators=[DataRequired(), URL(), Length(max=255)]
    )
    coordinates = StringField("Coordinates", validators=[Length(max=255)])
