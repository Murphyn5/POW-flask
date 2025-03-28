from app.models import db, CommunityEventImage, debug, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


# Adds a demo user, you can add other users here if you want
def seed_community_event_images():
    db.session.add(
        CommunityEventImage(
            url="/protest-saturday.jpeg",
            caption="",
            community_event_id=1,
        )
    )

    db.session.add(
        CommunityEventImage(
            url="/Feb-Watersheds-workshop.1-300x232.jpeg",
            caption="",
            community_event_id=2,
        )
    )

    db.session.add(
        CommunityEventImage(
            url="/waterinourhands.jpg",
            caption="",
            community_event_id=3,
        )
    )


    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.


def undo_community_event_images():
    if debug == 1:
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.community_event_images RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute(text("DELETE FROM community_event_images"))

    db.session.commit()
