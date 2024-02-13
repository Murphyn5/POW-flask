from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class MeetingImage(db.Model, UserMixin):
    __tablename__ = "meeting_images"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    meeting_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('meetings.id')))
    url = db.Column(db.String)
    caption = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


    meeting = db.relationship("Meeting", back_populates = "meeting_images")

    def to_dict(self):
        return {
            'id': self.id,
            'meeting_id': self.meeting_id,
            'url': self.url,
            'caption': self.caption,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }
