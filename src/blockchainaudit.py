from app import app, db
from app.models import City, Country, Office, User


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "City": City, "Country": Country, "Office": Office, "User": User}
