from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class Article(db.Model, UserMixin):
    __tablename__ = "articles"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    source = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)
    link = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    article_images = db.relationship(
        "ArticleImage", cascade="all, delete", back_populates="article")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'source': self.source,
            'date_posted': self.date_posted.isoformat() if self.date_posted else None,
            'link': self.link,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }
