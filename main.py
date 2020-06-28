from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from views import lists
from views.lists import lists_bp
from classes import Lists

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root1234@localhost/best_order_DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.register_blueprint(lists_bp, url_prefix="/lists")


@app.route("/lists")
def all_lists():

    result = "<table border=1>"
    for mylist in Lists.query.all():
        result += "<tr> <td>" + str(mylist.id) + "</td> " \
                       "<td>" + mylist.name + "</td>" \
                       "<td> " + mylist.description + "</td>" \
                  "</tr>"
    return result + "</table>" + "done"


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)