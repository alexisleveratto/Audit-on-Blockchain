from app import app, db
from app.models import Account, City, Country, Contract, Office, User


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Account": Account,
        "City": City,
        "Country": Country,
        "Contract": Contract,
        "Office": Office,
        "User": User,
    }
