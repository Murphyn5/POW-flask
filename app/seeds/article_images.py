from app.models import db, ArticleImage, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


# Adds a demo user, you can add other users here if you want
def seed_article_images():
    db.session.add(
        ArticleImage(
            url="/static/images/Yachats-Logo-200x200-01.jpg",
            caption="",
            article_id=1,
        )
    )

    db.session.add(
        ArticleImage(
            url="/static/images/USA-Oregon-Beaver-Creek-3724-copy-768x512.jpeg",
            caption="",
            article_id=2,
        )
    )

    db.session.add(
        ArticleImage(
            url="/static/images/coos-bay-aerial-marina.com_-768x512.jpg",
            caption="",
            article_id=3,
        )
    )

    db.session.add(
        ArticleImage(
            url="/static/images/20230709news-image_50387969-1300x844-1-300x195.jpg",
            caption="",
            article_id=4,
        )
    )

    db.session.add(
        ArticleImage(
            url="/static/images/ClimberAndBanner.jpg",
            caption="",
            article_id=5,
        )
    )

    db.session.add(
        ArticleImage(
            url="/static/images/The-view-from-atop-Kings-Mountain-summit-in-the-Tillamook…-_-Flickr.jpg",
            caption="The Tillamook State Forest as seen from the summit of King’s Mountain. Bare patches mark spots that have been clearcut. (Source: Oregon Department of Forestry/Flickr)",
            article_id=6,
        )
    )

    db.session.add(
        ArticleImage(
            url="/static/images/Drone-Screen-Shot-2023-08-14-at-10.11.40-AM-1536x503.png",
            caption="The image from a drone video shows some of the seven parcels in the South Beaver Creek watershed that will be ground sprayed with herbicides by Ane Forests of Oregon.By GARRET JAROS )",
            article_id=7,
        )
    )

    db.session.add(
        ArticleImage(
            url="/static/images/64f8d0d9aba72.image.jpg",
            caption="A lone protester stands along Highway 101 in Newport with a banner opposing aerial spraying of herbicides. (Photos by Tony Reed)",
            article_id=8,
        )
    )


    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.


def undo_article_images():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.article_images RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute(text("DELETE FROM article_images"))

    db.session.commit()
