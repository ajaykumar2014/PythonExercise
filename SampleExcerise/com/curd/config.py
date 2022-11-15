from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///university_lite_store.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
ma = Marshmallow(app)
db = SQLAlchemy(app)