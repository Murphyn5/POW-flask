from .db import db, debug, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class Meeting(db.Model, UserMixin):
    __tablename__ = "meetings"

    if debug == 1:
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    meeting_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    meeting_images = db.relationship(
        "MeetingImage", cascade="all, delete", back_populates="meeting")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'meeting_date': self.meeting_date,
            'description': self.description,
            'link': self.link,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }
