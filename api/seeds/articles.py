from datetime import datetime
from api.models import db, environment, SCHEMA, Article
from sqlalchemy.sql import text

def seed_articles():

    article1 = Article(
        title="Yachats News Editorial",
        source="Yachats News",
        date_posted=datetime(2023, 10, 23),  # Replace with an actual date
        link="https://yachatsnews.com/lincoln-county-residents-commissioners-should-oppose-timber-spraying/",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    article2 = Article(
        title="Science is the focus, chemical to be sprayed causes cancer",
        source="Newport NewsTimes",
        date_posted=datetime(2023, 9, 23),  # Replace with an actual date
        link="https://www.newportnewstimes.com/opinion/science-is-the-focus-chemical-to-be-sprayed-causes-cancer/article_15c8d06a-58c1-11ee-b080-8b1ef9a56407.html",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )


    article3 = Article(
        title="Legislative Action Causes Threat To Estuary",
        source="Newport NewsTimes",
        date_posted=datetime(2023, 9, 27),  # Replace with an actual date
        link="https://www.newportnewstimes.com/opinion/column-legislative-action-causes-threat-to-estuary/article_936f554a-525c-11ee-b7d6-af3df7789d16.html",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )


    article4 = Article(
        title="Lock Down For Old Growth",
        source="Eugene Weekly",
        date_posted=datetime(2023, 9, 26),  # Replace with an actual date
        link="https://eugeneweekly.com/2023/07/06/locked-down-for-old-growth-forests/",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    article5 = Article(
        title="Protestors Launch Tree Sit to Protect Old Growth",
        source="Cascadia Forest Defenders",
        date_posted=datetime(2023, 9, 26),  # Replace with an actual date
        link="https://forestdefensenow.wordpress.com/2021/09/14/protestors-launch-tree-sit-to-protect-old-growth-forest-from-logging/",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    article6 = Article(
        title="NASA Imagery Shows Impact of Logging in OR Coast Watersheds",
        source="Oregon Capital Chronicle",
        date_posted=datetime(2023, 9, 19),  # Replace with an actual date
        link="https://oregoncapitalchronicle.com/2023/09/19/nasa-imagery-shows-scale-impacts-of-logging-in-drinking-watersheds-on-oregon-coast/",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    article7 = Article(
        title="Timber company owner says it will not spray herbicides by helicopter in South Beaver Creek, but use ground crews instead",
        source="Yachats News",
        date_posted=datetime(2023, 9, 12),  # Replace with an actual date
        link="https://yachatsnews.com/timber-company-owner-says-it-will-not-spray-herbicides-by-helicopter-in-south-beaver-creek-but-use-ground-crews-instead/",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    article8 = Article(
        title="Opposition to Herbicide Spraying Continues",
        source="Newport NewsTimes",
        date_posted=datetime(2023, 9, 12),  # Replace with an actual date
        link="https://www.newportnewstimes.com/news/opposition-to-herbicide-spraying-continues/article_e56ebe82-4d9b-11ee-9535-0f38e4f36afa.html",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )


    # Add seed data to the database session
    db.session.add_all([article1, article2, article3, article4, article5, article6, article7, article8])

    # Commit the changes to the database
    db.session.commit()

def undo_articles():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.articles RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM articles"))

    db.session.commit()
