from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:toor@localhost/best_order_DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Lists(db.Model):
    __tablename__ = "list_table"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(225))
    description = db.Column(db.String(225))


class Tasks(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    list_id = db.Column(db.Integer)
    description = db.Column(db.String(225))
    status = db.Column(db.String(225))
    priority = db.Column(db.Integer)
    assignee = db.Column(db.String(225))


class Workers(db.Model):
    __tablename__ = "workers"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Integer)
    title = db.Column(db.String(225))
