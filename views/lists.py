from flask import Blueprint
lists_bp = Blueprint("lists_bp", __name__)


@lists_bp.route("/add_list")
def add_list():
    return "add_list"


@lists_bp.route("/edit_list")
def edit_list():
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
