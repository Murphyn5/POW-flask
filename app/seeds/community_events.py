from datetime import datetime
from app.models import db, debug, SCHEMA, CommunityEvent
from sqlalchemy.sql import text

def seed_community_events():

    community_event1 = CommunityEvent(
        title="PUBLIC PROTEST",
        days="Saturdays",
        dates="",
        times="11:00 AM to 1:00 PM",
        location="WALDPORT Hwy 101 and 34",
        description="Our chance to make some noise and build community support!",
        link="",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    community_event2 = CommunityEvent(
        title="Drinking Water Protection",
        days="Tuesday",
        dates="Feb. 6, 2024",
        times="12:00 pm to 4:30 pm",
        location="OCCC Newport Campus",
        description="These workshops are designed for communities to collaborate with fellow drinking water providers, local governments, conservation practitioners, land managers, and funding partners. In-person and virtual options available.",
        link="https://www.oregon.gov/deq/wq/programs/pages/water-protection-workshops.aspx",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    community_event3 = CommunityEvent(
        title="Caring For Our Water",
        days="Wednesdays",
        dates="Feb 28, Mar 6, Mar 13, Mar 20",
        times="6-7:30 pm",
        location="OCCC Waldport Campus",
        description="Drinking water comes from our faucets but how does it get there? When we look at water, it looks clean, but is it? Come join us for a 4 session class and find answers to these water related questions.  Let’s look at the how our daily choices and the corporate world impacts the around water.",
        link="https://www.oregon.gov/deq/wq/programs/pages/water-protection-workshops.aspx",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )


    # Add seed data to the database session
    db.session.add_all([community_event1, community_event2, community_event3])

    # Commit the changes to the database
    db.session.commit()

def undo_community_events():
    if debug == 1:
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.community_events RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM community_events"))

    db.session.commit()
