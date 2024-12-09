# Import dependencies
from flask import Flask
from flask import render_template
from flask import request
import db_manager

# Create an instance of the Flask class in the app variable
app = Flask(__name__)

is_logged_in = False

# Define the route for the index page at domain root
@app.route("/", methods=["POST", "GET"])
def index_page():
    global is_logged_in
    if request.method == "POST":
        if request.form["password"].isdigit():
            password = int(request.form["password"])
            email = request.form["email"]
            is_logged_in = db_manager.check_login(email, password)
        app.logger.critical(f"{email} is logged in ? {is_logged_in}")
    #print("Debug: Start of index_page")
    return render_template("index.html", is_logged_in=is_logged_in), 200


# Initialize the Flask application
if __name__ == "__main__":
    app.run(debug=True)
