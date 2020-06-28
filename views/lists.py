from flask import Blueprint, Flask
from flask_sqlalchemy import SQLAlchemy
from classes import Lists

lists_bp = Blueprint("lists_bp", __name__)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root1234@localhost/school'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@lists_bp.route("/add_list/<name>/<description>")
def add_list(name, description):
    new_list_item = Lists()
    new_list_item.name = name
    new_list_item.description = description
    db.session.add(new_list_item)
    db.session.commit()
    return "Done new list item added to lists list"


@lists_bp.route("/edit_list/<id>/<name>/<description>")
def edit_list(id, name, description):
    Lists.query.filter(Lists.id == id).update({"name": name})
    Lists.query.filter(Lists.id == id).update({"description": description})
    db.session.commit()
    return "edit_list"


@lists_bp.route("/delete_list/<id>")
def delete_list(id):
    itemtoremove = Lists.query.filter(Lists.id == id)

    db.session.commit()
    return "edit_list"


@lists_bp.route("/view_tasks")
def view_tasks():
    return "view_tasks"


@lists_bp.route("/add_task")
def add_task():
    return "add_task"


@lists_bp.route("/edit_task")
def edit_task():
    return "edit_task"
