from .db import db, debug, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class ArticleImage(db.Model, UserMixin):
    __tablename__ = "article_images"

    if debug == 1:
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("articles.id")))
    url = db.Column(db.String, nullable=False)
    caption = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    article = db.relationship("Article", back_populates = "article_images")

    def to_dict(self):
        return {
            'id': self.id,
            'article_id': self.article_id,
            'url': self.url,
            'caption': self.caption,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }
