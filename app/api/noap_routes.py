from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from .auth_routes import validation_errors_to_error_messages
from app.models import db, Noap
from datetime import datetime
from app.forms.noaps_form import NoapForm

noap_routes = Blueprint("noaps", __name__)


# CREATE NEW NOAP
@noap_routes.route("/", methods=["POST"])
@login_required
def create_new_noap():
    form = NoapForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    data = request.get_json()
    if form.validate_on_submit():
        new_noap = Noap(
            noap_id=data["noap_id"],
            operation_name=data["operation_name"],
            report_filed=data["report_filed"],
            fully_implemented_written_plan=data["fully_implemented_written_plan"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            permit_link=data["permit_link"],
            ferns_link=data["ferns_link"],
            coordinates=data["coordinates"],
            updated_at=datetime.utcnow(),
            created_at=datetime.utcnow(),
        )
        db.session.add(new_noap)
        db.session.commit()
        new_noap = new_noap.to_dict()
        return new_noap
    if form.errors:
        return {
            "message": "Validation error",
            "statusCode": 400,
            "errors": validation_errors_to_error_messages(form.errors),
        }, 400


# GET ALL NOAPS
@noap_routes.route("/")
def get_noaps():
    noaps = Noap.query.all()
    noaps_to_return = []

    for noap in noaps:
        noap_dict = noap.to_dict()
        noaps_to_return.append(noap_dict)

    return {"noaps": {noap_dict["id"]: noap_dict for noap_dict in noaps_to_return}}


# UPDATE NOAP
@noap_routes.route("/<int:id>", methods=["PUT"])
@login_required
def update_noap(id):
    noap = Noap.query.get(id)
    if not noap:
        return {
            "errors": ["error: Noap couldn't be found"],
            "status_code": 404,
        }, 404
    data = request.get_json()
    # dt = datetime.strptime(data["date_time"], "%Y-%m-%d %H:%M:%S")
    form = NoapForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        noap.noap_id = (data["noap_id"],)
        noap.operation_name = (data["operation_name"],)
        noap.fully_implemented_written_plan = (data["fully_implemented_written_plan"],)
        noap.start_date = (data["start_date"],)
        noap.end_date = (data["end_date"],)
        noap.permit_link = (data["permit_link"],)
        noap.ferns_link = (data["ferns_link"],)
        noap.coordinates = (data["coordinates"],)
        noap.updated_at = (datetime.utcnow(),)
        db.session.commit()
        noap_dict = noap.to_dict()
        return noap_dict, 200
    if form.errors:
        return {
            "message": "Validation error",
            "statusCode": 400,
            "errors": validation_errors_to_error_messages(form.errors),
        }, 400


# DELETE A NOAP
@noap_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_noap(id):
    noap = Noap.query.get(id)

    if not noap:
        return {"errors": "error: Noap couldn't be found", "status_code": 404}, 404

    db.session.delete(noap)
    db.session.commit()
    return {"message": "Successfully deleted", "status_code": 200}
