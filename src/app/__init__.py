from config import Config
from flask import Flask


app = Flask(__name__)
app.config.from_object(Config)
print(app.config["SECRET_KEY"])
from app import routes
