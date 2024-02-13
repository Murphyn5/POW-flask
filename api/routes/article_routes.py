from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from .auth_routes import validation_errors_to_error_messages
from api.models import db, User, Article, ArticleImage
from datetime import datetime
from api.forms.articles_form import ArticleForm
from api.forms.article_images_form import ArticleImageForm

article_routes = Blueprint("articles", __name__)

# CREATE NEW ARTICLE
@article_routes.route("/", methods=["POST"])
@login_required
def create_new_article():
    form = ArticleForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    data = request.get_json()
    dt = datetime.strptime(data["date_posted"], "%Y-%m-%d %H:%M:%S")
    if form.validate_on_submit():
        new_article = Article(
            title=data["title"],
            source=data["source"],
            link=data["link"],
            date_posted=dt,
            updated_at=datetime.utcnow(),
            created_at=datetime.utcnow(),
        )
        db.session.add(new_article)
        db.session.commit()
        new_article = new_article.to_dict()
        return new_article
    if form.errors:
        return {
            "message": "Validation error",
            "statusCode": 400,
            "errors": validation_errors_to_error_messages(form.errors),
        }, 400


# GET ALL ARTICLES
@article_routes.route("/")
def get_articles():
    articles = Article.query.all()
    articles_to_return = []

    for article in articles:
        article_dict = article.to_dict()
        images_length = len(article.article_images)
        article_dict["images_length"] = images_length
        article_dict["images"] = []
        for image in article.article_images:
            article_dict["images"].append(image.to_dict())
        articles_to_return.append(article_dict)

    return {
        "articles": {
            article_dict["id"]: article_dict for article_dict in articles_to_return
        }
    }


# UPDATE ARTICLE
@article_routes.route("/<int:id>", methods=["PUT"])
@login_required
def update_article(id):
    article = Article.query.get(id)
    if not article:
        return {
            "errors": ["error: Article couldn't be found"],
            "status_code": 404,
        }, 404
    data = request.get_json()
    dt = datetime.strptime(data["date_posted"], "%Y-%m-%d %H:%M:%S")
    form = ArticleForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        article.title = data["title"]
        article.source = data["source"]
        article.link = data["link"]
        article.date_posted = dt
        article.updated_at = datetime.utcnow()
        db.session.commit()
        article_dict = article.to_dict()
        return article_dict, 200
    if form.errors:
        return {
            "message": "Validation error",
            "statusCode": 400,
            "errors": validation_errors_to_error_messages(form.errors),
        }, 400


# DELETE AN ARTICLE
@article_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_article(id):
    article = Article.query.get(id)

    if not article:
        return {"errors": "error: Article couldn't be found", "status_code": 404}, 404

    db.session.delete(article)
    db.session.commit()
    return {"message": "Successfully deleted", "status_code": 200}


# CREATE NEW IMAGE FOR AN ARTICLE
@article_routes.route("/<int:id>/images", methods=["POST"])
@login_required
def create_new_image(id):
    article = Article.query.get(id)
    if not article:
        return {"errors": "Article couldn't be found", "status_code": 404}, 404

    form = ArticleImageForm()

    form["csrf_token"].data = request.cookies["csrf_token"]
    data = form.data

    if form.validate_on_submit():
        new_article_image = ArticleImage(
            article_id=id,
            url=data["url"],
            caption=data["caption"],
            updated_at=datetime.utcnow(),
            created_at=datetime.utcnow(),
        )
        db.session.add(new_article_image)
        db.session.commit()
        new_article_image = new_article_image.to_dict()
        return new_article_image
    if form.errors:
        return {
            "message": "Validation error",
            "statusCode": 400,
            "errors": validation_errors_to_error_messages(form.errors),
        }, 400
