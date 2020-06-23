from flask import Flask, render_template, request
from views.lists import lists_bp
app = Flask(__name__)
app = Flask(__name__)
app.register_blueprint(lists_bp, url_prefix="/lists")


@app.route("/lists")
def mainpage():
    return render_template("main.html")


if __name__ == "__main__":
    app.run(host="localhost", port=9191, debug=True)