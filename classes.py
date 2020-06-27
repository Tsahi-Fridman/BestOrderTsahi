from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:toor@localhost/best_order_DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Lists(db.Model):
    __tablename__ = "lists"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(225))
    description = db.Column(db.String(225))

    def __init__(self):
        print("__init__")

    def add_list(self):
        print("add_list")

    def edit_list(self):
        print("add_list")

    def delete_list(self):
        print("add_list")


class Tasks(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    list_id = db.Column(db.Integer)
    description = db.Column(db.String(225))
    status = db.Column(db.String(225))
    priority = db.Column(db.Integer)
    assignee = db.Column(db.String(225))

    # description VARCHAR(255), status VARCHAR(255), priority INTEGER(20), assignee  VARCHAR(255)

    def __init__(self):
        print("__init__")

    def add_list(self):
        print("add_list")

    def edit_list(self):
        print("add_list")

    def delete_list(self):
        print("add_list")