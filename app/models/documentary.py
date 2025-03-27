from .db import db, debug, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class Documentary(db.Model, UserMixin):
    __tablename__ = "documentaries"

    if debug == 1:
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    source = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    documentary_images = db.relationship(
        "DocumentaryImage", cascade="all, delete", back_populates="documentary")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'source': self.source,
            'description': self.description,
            'link': self.link,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }
