from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

is_logged_in = False


@app.route("/", methods=["POST", "GET"])
def index_page():
    global is_logged_in
    if request.method == "POST":
        username = request.form["username"]
        app.logger.critical(f"Username is {username}")
        password = request.form["password"]
        app.logger.critical(f"Password is {password}")
        is_logged_in = True
        app.logger.critical(f"User is logged in ? {is_logged_in}")
    return render_template("index.html", is_logged_in=is_logged_in), 200


if __name__ == "__main__":
    app.run(debug=True)
