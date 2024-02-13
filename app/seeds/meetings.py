from datetime import datetime
from app.models import db, environment, SCHEMA, Meeting
from sqlalchemy.sql import text

def seed_meetings():

    meeting1 = Meeting(
        title="Oregon Community Rights Network",
        description="Kai Huschke, from Oregon Community Rights Network, spoke on grassroots organizing for local decision-making and how it relates to the legalized spraying of toxic chemicals over the Beaver Creek watershed. More information about ORCN- Oregon Community Rights Network’s mission is to support and empower communities to secure local self determination and self-governance rights, superior to corporate power, in order to protect fundamental rights, quality of life, the natural environment, public health, and safety. Visit orcrn.org to learn more",
        meeting_date=datetime(2023, 9, 24),
        link="https://www.youtube.com/watch?v=F0_zd35ZUBg",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    # Add seed data to the database session
    db.session.add_all([meeting1])

    # Commit the changes to the database
    db.session.commit()

def undo_meetings():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.meetings RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM meetings"))

    db.session.commit()
