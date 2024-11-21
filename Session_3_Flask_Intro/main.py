# Import dependencies
from flask import Flask
from flask import render_template
from flask import request

# Create an instance of the Flask class in the app variable
app = Flask(__name__)


# Define the route for the index page at domain root
@app.route("/", methods=["POST", "GET"])
def index_page():
    return render_template("index.html"), 200


# Initialize the Flask application
if __name__ == "__main__":
    app.run(debug=True)
