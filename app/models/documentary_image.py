from .db import db, debug, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class DocumentaryImage(db.Model, UserMixin):
    __tablename__ = "documentary_images"

    if debug == 1:
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    documentary_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("documentaries.id")))
    url = db.Column(db.String, nullable=False)
    caption = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    documentary = db.relationship("Documentary", back_populates = "documentary_images")

    def to_dict(self):
        return {
            "id": self.id,
            "documentary_id": self.documentary_id,
            "url": self.url,
            "caption": self.caption,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
