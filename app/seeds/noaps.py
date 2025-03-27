from datetime import datetime
from app.models import db, debug, SCHEMA, Noap
from sqlalchemy.sql import text

def seed_noaps():

    noap1 = Noap(
        noap_id="2023-553-10589",
        operation_name="Pankey Pit Clear Cut (above Eckman Lake)",
        report_filed=datetime(2023, 9, 21),
        fully_implemented_written_plan=datetime(2023, 10, 9),
        start_date=datetime(2023, 10, 9),
        end_date=datetime(2023, 12, 31),
        permit_link="https://ferns.odf.oregon.gov/E-Notification/noap/175284/Report/Summary",
        ferns_link="https://ferns.odf.oregon.gov/E-Notification/noap/175284?View=Summary",
        coordinates="40.7128° N, 74.0060° W"
    )

    noap2 = Noap(
        noap_id="2023-553-09307",
        operation_name="South Beaver Creek Aerial Spray",
        report_filed=datetime(2023, 8, 2),
        fully_implemented_written_plan=datetime(2023, 8, 18),
        start_date=datetime(2023, 9, 2),
        end_date=datetime(2023, 11, 30),
        permit_link="https://ferns.odf.oregon.gov/E-Notification/noap/173409/Report/Summary",
        ferns_link="https://ferns.odf.oregon.gov/E-Notification/noap/173409?View=Summary&fbclid=IwAR09WyFsBbq8oRGXqpGXvjQgBEcQCL4R8dcSsFXhcpqGwh4snRRJNGy3Nz8",
        coordinates="34.0522° N, 118.2437° W"
    )

    noap3 = Noap(
        noap_id="2023-552-10095",
        operation_name="South Beaver Creek Backpack Spray",
        report_filed=datetime(2023, 8, 30),
        fully_implemented_written_plan=datetime(2023, 9, 13),
        start_date=datetime(2023, 9, 13),
        end_date=datetime(2023, 11, 30),
        permit_link="https://ferns.odf.oregon.gov/E-Notification/noap/174630/Report/Summary",
        ferns_link="https://ferns.odf.oregon.gov/E-Notification/noap/174630?View=Summary",
        coordinates="34.0522° N, 118.2437° W"
    )

    noap4 = Noap(
        noap_id="2024-553-00161",
        operation_name="2024 Lincoln County Road Maintenance",
        report_filed=datetime(2023, 12, 4),
        start_date=datetime(2024, 1, 1),
        end_date=datetime(2024, 12, 31),
        permit_link="https://ferns.odf.oregon.gov/E-Notification/noap/177371/Report/Summary",
        ferns_link="https://ferns.odf.oregon.gov/E-Notification/noap/177371?View=Summary",
        coordinates="34.0522° N, 118.2437° W"
    )


    # Add seed data to the database session
    db.session.add_all([noap1, noap2, noap3, noap4])

    # Commit the changes to the database
    db.session.commit()

def undo_noaps():
    if debug == 1:
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.noaps RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM noaps"))

    db.session.commit()
