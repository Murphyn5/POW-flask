from datetime import datetime
from app.models import db, debug, SCHEMA, Documentary
from sqlalchemy.sql import text


def seed_documentaries():
    documentary1 = Documentary(
        title="A Testimony: Beaver Creek Residents Unite!",
        source="Willow Kasner",
        description="A story about Beaver Creek residents",
        link="https://www.youtube.com/watch?v=zyBP1BHMEAg",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    documentary2 = Documentary(
        title="Siletz Gorge to the Valley of the Giants",
        source="Lincoln County Community Rights",
        description="15 minute tour through our beautiful Siletz Gorge",
        link="https://www.youtube.com/watch?v=RtF1gMBVm94",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    documentary3 = Documentary(
        title="Valley of the Giants: Coast Range’s gift of intact Old Growth Forest",
        source="Lincoln County Community Rights",
        description="Tour through  the forest",
        link="https://www.youtube.com/watch?v=e_ww0H0Xx10",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    documentary4 = Documentary(
        title="Big Creek Tour: 3 minutes on aerial spraying",
        source="Lincoln County Community Rights",
        description="Newport water is from Big Creek- how much has been sprayed?",
        link="https://www.youtube.com/watch?v=LQ3ccOwn054",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    documentary5 = Documentary(
        title="My Experience With Pesticides: It effected my whole family",
        source="Loren, A Farm Owner",
        description="A heart felt story about a farmer, his wife and family",
        link="https://www.youtube.com/watch?v=AbwqEOdAJQo&feature=youtu.be",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    documentary6 = Documentary(
        title="Hot Spot for Birth Defects: Excerpt 1",
        source="Renee Stringham, MD",
        description="Lincoln County stories of medical practices & politics, research & activism",
        link="https://www.youtube.com/watch?v=D9BURFN5P9k",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    documentary7 = Documentary(
        title="Hot Spot for Birth Defects: Excerpt 2",
        source="Renee Stringham, MD",
        description="Lincoln County stories of medical practices & politics, research & activism",
        link="https://www.youtube.com/watch?v=HRXCjXdUt2k",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    documentary8 = Documentary(
        title="Citizens for a Healthy County: Harvard Economist talks Forest",
        source="Ernie Niemi, Economist ",
        description="Economic Picture of Forestry in Lincoln County",
        link="https://www.youtube.com/watch?v=XXOlen9PQs0",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    documentary9 = Documentary(
        title="Regulatory Whiplash: Federalist Society",
        source="Will Trackman & Adam White",
        description="Transferring power from one political party to the next",
        link="https://www.youtube.com/watch?v=_UA7Msyk3cE",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    documentary10 = Documentary(
        title="Water- Earth’s Blood: The old and new water Paradigm",
        source="Zachary Weiss",
        description="Restoring our Planet’s Health",
        link="https://www.youtube.com/watch?v=Vik4vUN3SPI",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    documentary11 = Documentary(
        title="The People vs Agent Orange: Summary",
        source="Citizen Representatives from Oregon Coast",
        description="Direct experience regarding aerial sprayings",
        link="https://www.youtube.com/watch?v=gL8i9KUEnog",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    documentary12 = Documentary(
        title="The People vs Agent Orange: Panel Discussion",
        source="Citizen Representatives from Oregon Coast",
        description="Direct experience regarding aerial sprayings",
        link="https://www.youtube.com/watch?v=gUfZrfpUalU",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    documentary13 = Documentary(
        title="DRIFT: A Community Seeking Justice",
        source="Beyond Toxics",
        description="A story about Gold Beach, OR residents",
        link="https://www.youtube.com/watch?app=desktop&v=_2cLCuFIa_k",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    documentary14 = Documentary(
        title="Regenerating A Forest with Goats",
        source="Happen Films",
        description="An environmentally safe alternative to herbicides",
        link="https://www.youtube.com/watch?v=g9yiclBCxMo&t=1s",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    documentary15 = Documentary(
        title="Toxics on Trial: Legal Legacies in Pesticide Reform",
        source="Northwest Center for Alternatives to Pesticides",
        description="Full trial on chemical exposure to pesticides and herbicides and their effects on ecosystems",
        link="https://www.youtube.com/watch?v=EVI4FlEbxy4",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    documentary16 = Documentary(
        title="Behind the Emerald Curtain",
        source="Pacific Rivers TV",
        description="Asking for a balance in Forest Management",
        link="https://www.youtube.com/watch?v=YDgzOcsNm9g",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    documentary17 = Documentary(
        title="How Beavers Engineer the Land",
        source="George Monbiot",
        description="Beavers are essential to water and land management",
        link="https://www.youtube.com/watch?v=Hy_WE9NAzY4",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    documentary18 = Documentary(
        title="Putting Forest First ",
        source="Peter Hayes, Hyla woods President",
        description="Forest are managed to support clean water and air.",
        link="https://www.youtube.com/watch?v=6lto7sR2O7w",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    # Add seed data to the database session
    db.session.add_all(
        [
            documentary1,
            documentary2,
            documentary3,
            documentary4,
            documentary5,
            documentary6,
            documentary7,
            documentary8,
            documentary9,
            documentary10,
            documentary11,
            documentary12,
            documentary13,
            documentary14,
            documentary15,
            documentary16,
            documentary17,
            documentary18
        ]
    )

    # Commit the changes to the database
    db.session.commit()


def undo_documentaries():
    if debug == 1:
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.documentaries RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute(text("DELETE FROM documentaries"))

    db.session.commit()
