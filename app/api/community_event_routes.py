from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from .auth_routes import validation_errors_to_error_messages
from app.models import db, User, CommunityEvent, CommunityEventImage
from datetime import datetime
from app.forms.community_events_form import CommunityEventForm
from app.forms.community_event_images_form import CommunityEventImageForm

community_event_routes = Blueprint("community_events", __name__)


# CREATE NEW COMMUNITY EVENT
@community_event_routes.route("/", methods=["POST"])
@login_required
def create_community_event():
    form = CommunityEventForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    data = request.get_json()
    # dt = datetime.strptime(data["date_time"], "%Y-%m-%d %H:%M:%S")
    if form.validate_on_submit():
        community_event = CommunityEvent(
            title=data["title"],
            days=data["days"],
            dates=data["dates"],
            times=data["times"],
            location=data["location"],
            description=data["description"],
            link=data["link"],
            updated_at=datetime.utcnow(),
            created_at=datetime.utcnow(),
        )
        db.session.add(community_event)
        db.session.commit()
        community_event = community_event.to_dict()
        return community_event
    if form.errors:
        return {
            "message": "Validation error",
            "statusCode": 400,
            "errors": validation_errors_to_error_messages(form.errors),
        }, 400


# GET ALL COMMUNITY EVENTS
@community_event_routes.route("/")
def get_community_events():
    community_events = CommunityEvent.query.all()
    community_events_to_return = []

    for community_event in community_events:
        community_event_dict = community_event.to_dict()
        images_length = len(community_event.community_event_images)
        community_event_dict["images_length"] = images_length
        community_event_dict["images"] = []
        for image in community_event.community_event_images:
            community_event_dict["images"].append(image.to_dict())
        community_events_to_return.append(community_event_dict)

    return {
        "community_events": {
            community_event_dict["id"]: community_event_dict for community_event_dict in community_events_to_return
        }
    }


# UPDATE COMMUNITY EVENT
@community_event_routes.route("/<int:id>", methods=["PUT"])
@login_required
def update_community_event(id):
    community_event = CommunityEvent.query.get(id)
    if not community_event:
        return {
            "errors": ["error: CommunityEvent couldn't be found"],
            "status_code": 404,
        }, 404
    data = request.get_json()
    # dt = datetime.strptime(data["date_time"], "%Y-%m-%d %H:%M:%S")
    form = CommunityEventForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        community_event.title = data["title"]
        community_event.days = data["days"]
        community_event.dates = data["dates"]
        community_event.times = data["times"]
        community_event.location = data["location"]
        community_event.description = data["description"]
        community_event.link = data["link"]
        community_event.updated_at = datetime.utcnow()
        db.session.commit()
        community_event_dict = community_event.to_dict()
        return community_event_dict, 200
    if form.errors:
        return {
            "message": "Validation error",
            "statusCode": 400,
            "errors": validation_errors_to_error_messages(form.errors),
        }, 400


# DELETE A COMMUNITY EVENT
@community_event_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_community_event(id):
    community_event = CommunityEvent.query.get(id)

    if not community_event:
        return {"errors": "error: Community Event couldn't be found", "status_code": 404}, 404

    db.session.delete(community_event)
    db.session.commit()
    return {"message": "Successfully deleted", "status_code": 200}


# CREATE NEW IMAGE FOR A COMMUNITY EVENT
@community_event_routes.route("/<int:id>/images", methods=["POST"])
@login_required
def create_new_image(id):
    community_event = CommunityEvent.query.get(id)
    if not community_event:
        return {"errors": "Community Event couldn't be found", "status_code": 404}, 404

    form = CommunityEventImageForm()

    form["csrf_token"].data = request.cookies["csrf_token"]
    data = form.data

    if form.validate_on_submit():
        community_event_image = CommunityEventImage(
            community_event_id=id,
            url=data["url"],
            caption=data["caption"],
            updated_at=datetime.utcnow(),
            created_at=datetime.utcnow(),
        )
        db.session.add(community_event_image)
        db.session.commit()
        community_event_image = community_event_image.to_dict()
        return community_event_image

    if form.errors:
        return {
            "message": "Validation error",
            "statusCode": 400,
            "errors": validation_errors_to_error_messages(form.errors),
        }, 400
