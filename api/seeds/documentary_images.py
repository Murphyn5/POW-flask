from api.models import db, DocumentaryImage, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


# Adds a demo user, you can add other users here if you want
def seed_documentary_images():
    db.session.add(
        DocumentaryImage(
            url="https://i3.ytimg.com/vi/zyBP1BHMEAg/maxresdefault.jpg",
            caption="",
            documentary_id=1,
        )
    )

    db.session.add(
        DocumentaryImage(
            url="https://i3.ytimg.com/vi/RtF1gMBVm94/maxresdefault.jpg",
            caption="",
            documentary_id=2,
        )
    )

    db.session.add(
        DocumentaryImage(
            url="http://i3.ytimg.com/vi/e_ww0H0Xx10/hqdefault.jpg",
            caption="",
            documentary_id=3,
        )
    )

    db.session.add(
        DocumentaryImage(
            url="http://i3.ytimg.com/vi/LQ3ccOwn054/hqdefault.jpg",
            caption="",
            documentary_id=4,
        )
    )

    db.session.add(
        DocumentaryImage(
            url="https://i3.ytimg.com/vi/AbwqEOdAJQo/maxresdefault.jpg",
            caption="",
            documentary_id=5,
        )
    )

    db.session.add(
        DocumentaryImage(
            url="https://i3.ytimg.com/vi/D9BURFN5P9k/maxresdefault.jpg",
            caption="",
            documentary_id=6,
        )
    )

    db.session.add(
        DocumentaryImage(
            url="https://i3.ytimg.com/vi/HRXCjXdUt2k/maxresdefault.jpg",
            caption="",
            documentary_id=7,
        )
    )

    db.session.add(
        DocumentaryImage(
            url="http://i3.ytimg.com/vi/XXOlen9PQs0/hqdefault.jpg",
            caption="",
            documentary_id=8,
        )
    )

    db.session.add(
        DocumentaryImage(
            url="https://i3.ytimg.com/vi/_UA7Msyk3cE/maxresdefault.jpg",
            caption="",
            documentary_id=9,
        )
    )

    db.session.add(
        DocumentaryImage(
            url="https://i3.ytimg.com/vi/Vik4vUN3SPI/maxresdefault.jpg",
            caption="",
            documentary_id=10,
        )
    )

    db.session.add(
        DocumentaryImage(
            url="https://i3.ytimg.com/vi/gL8i9KUEnog/maxresdefault.jpg",
            caption="",
            documentary_id=11,
        )
    )

    db.session.add(
        DocumentaryImage(
            url="http://i3.ytimg.com/vi/gUfZrfpUalU/hqdefault.jpg",
            caption="",
            documentary_id=12,
        )
    )

    db.session.add(
        DocumentaryImage(
            url="https://i3.ytimg.com/vi/_2cLCuFIa_k/maxresdefault.jpg",
            caption="",
            documentary_id=13,
        )
    )

    db.session.add(
        DocumentaryImage(
            url="https://i3.ytimg.com/vi/g9yiclBCxMo/maxresdefault.jpg",
            caption="",
            documentary_id=14,
        )
    )

    db.session.add(
        DocumentaryImage(
            url="http://i3.ytimg.com/vi/EVI4FlEbxy4/hqdefault.jpg",
            caption="",
            documentary_id=15,
        )
    )

    db.session.add(
        DocumentaryImage(
            url="https://i3.ytimg.com/vi/YDgzOcsNm9g/maxresdefault.jpg",
            caption="",
            documentary_id=16,
        )
    )

    db.session.add(
        DocumentaryImage(
            url="https://i3.ytimg.com/vi/Hy_WE9NAzY4/maxresdefault.jpg",
            caption="",
            documentary_id=17,
        )
    )

    db.session.add(
        DocumentaryImage(
            url="https://i3.ytimg.com/vi/6lto7sR2O7w/maxresdefault.jpg",
            caption="",
            documentary_id=18,
        )
    )

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.


def undo_documentary_images():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.documentary_images RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute(text("DELETE FROM documentary_images"))

    db.session.commit()
