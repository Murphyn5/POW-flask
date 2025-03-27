from .db import db, debug, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class CommunityEvent(db.Model, UserMixin):
    __tablename__ = "community_events"

    if debug == 1:
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    days = db.Column(db.String)
    dates = db.Column(db.String)
    times = db.Column(db.String)
    location = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    link = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    community_event_images = db.relationship(
        "CommunityEventImage", cascade="all, delete", back_populates="community_event")

    def to_dict(self):
        return {
            "id": self.id,
            "days": self.days,
            "dates": self.dates,
            "times": self.times,
            "location": self.location,
            "title": self.title,
            "description": self.description,
            "link": self.link,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
