from app.models import db, MeetingImage, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


# Adds a demo user, you can add other users here if you want
def seed_meeting_images():
    db.session.add(
        MeetingImage(
            url="/recordedmeeting1.jpeg",
            caption="",
            meeting_id=1,
        )
    )

    db.session.add(
        MeetingImage(
            url="/OCRN.png",
            caption="",
            meeting_id=1,
        )
    )


    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.


def undo_meeting_images():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.meeting_images RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute(text("DELETE FROM meeting_images"))

    db.session.commit()
