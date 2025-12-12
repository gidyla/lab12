# my_project/setup.py
from my_project import create_app, db

app = create_app()

with app.app_context():
    db.create_all()  # Create all tables in the database