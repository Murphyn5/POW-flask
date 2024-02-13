from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from .auth_routes import validation_errors_to_error_messages
from app.models import db, User, Documentary, DocumentaryImage
from datetime import datetime
from app.forms.documentaries_form import DocumentaryForm
from app.forms.documentary_images_form import DocumentaryImageForm

documentary_routes = Blueprint("documentaries", __name__)


# CREATE NEW DOCUMENTARY
@documentary_routes.route("/", methods=["POST"])
@login_required
def create_new_documentary():
    form = DocumentaryForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    data = request.get_json()
    # dt = datetime.strptime(data["date_time"], "%Y-%m-%d %H:%M:%S")
    if form.validate_on_submit():
        new_documentary = Documentary(
            title=data["title"],
            source=data["source"],
            link=data["link"],
            description=data["description"],
            updated_at=datetime.utcnow(),
            created_at=datetime.utcnow(),
        )
        db.session.add(new_documentary)
        db.session.commit()
        new_documentary = new_documentary.to_dict()
        return new_documentary
    if form.errors:
        return {
            "message": "Validation error",
            "statusCode": 400,
            "errors": validation_errors_to_error_messages(form.errors),
        }, 400


# GET ALL DOCUMENTARYS
@documentary_routes.route("/")
def get_documentaries():
    documentaries = Documentary.query.all()
    documentaries_to_return = []

    for documentary in documentaries:
        documentary_dict = documentary.to_dict()
        images_length = len(documentary.documentary_images)
        documentary_dict["images_length"] = images_length
        documentary_dict["images"] = []
        for image in documentary.documentary_images:
            documentary_dict["images"].append(image.to_dict())
        documentaries_to_return.append(documentary_dict)

    return {
        "documentaries": {
            documentary_dict["id"]: documentary_dict for documentary_dict in documentaries_to_return
        }
    }


# UPDATE DOCUMENTARY
@documentary_routes.route("/<int:id>", methods=["PUT"])
@login_required
def update_documentary(id):
    documentary = Documentary.query.get(id)
    if not documentary:
        return {
            "errors": ["error: Documentary couldn't be found"],
            "status_code": 404,
        }, 404
    data = request.get_json()
    # dt = datetime.strptime(data["date_time"], "%Y-%m-%d %H:%M:%S")
    form = DocumentaryForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        documentary.title = data["title"]
        documentary.source = data["source"]
        documentary.link = data["link"]
        documentary.description = data["description"]
        documentary.updated_at = datetime.utcnow()
        db.session.commit()
        documentary_dict = documentary.to_dict()
        return documentary_dict, 200
    if form.errors:
        return {
            "message": "Validation error",
            "statusCode": 400,
            "errors": validation_errors_to_error_messages(form.errors),
        }, 400


# DELETE A DOCUMENTARY
@documentary_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_documentary(id):
    documentary = Documentary.query.get(id)

    if not documentary:
        return {"errors": "error: Documentary couldn't be found", "status_code": 404}, 404

    db.session.delete(documentary)
    db.session.commit()
    return {"message": "Successfully deleted", "status_code": 200}


# CREATE NEW IMAGE FOR A DOCUMENTARY
@documentary_routes.route("/<int:id>/images", methods=["POST"])
@login_required
def create_new_image(id):
    documentary = Documentary.query.get(id)
    if not documentary:
        return {"errors": "Documentary couldn't be found", "status_code": 404}, 404

    form = DocumentaryImageForm()

    form["csrf_token"].data = request.cookies["csrf_token"]
    data = form.data

    if form.validate_on_submit():
        new_documentary_image = DocumentaryImage(
            documentary_id=id,
            url=data["url"],
            caption=data["caption"],
            updated_at=datetime.utcnow(),
            created_at=datetime.utcnow(),
        )
        db.session.add(new_documentary_image)
        db.session.commit()
        new_documentary_image = new_documentary_image.to_dict()
        return new_documentary_image
    if form.errors:
        return {
            "message": "Validation error",
            "statusCode": 400,
            "errors": validation_errors_to_error_messages(form.errors),
        }, 400
