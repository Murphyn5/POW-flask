from app.models import db, CommunityEventImage, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


# Adds a demo user, you can add other users here if you want
def seed_community_event_images():
    db.session.add(
        CommunityEventImage(
            url="/static/images/PROTESt-Saturdays-1-300x225.jpeg",
            caption="",
            community_event_id=1,
        )
    )

    db.session.add(
        CommunityEventImage(
            url="/static/images/Feb-Watersheds-workshop.jpeg",
            caption="",
            community_event_id=2,
        )
    )

    db.session.add(
        CommunityEventImage(
            url="/static/images/OcccWaterIsInOurHands.jpg",
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
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.community_event_images RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute(text("DELETE FROM community_event_images"))

    db.session.commit()
