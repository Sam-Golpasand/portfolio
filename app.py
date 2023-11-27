from flask import Flask, redirect, render_template, request, session, flash, url_for
from flask_bcrypt import Bcrypt
from flask_session import Session



app = Flask(__name__)

Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(Exception)
def handle_error(error):
    return f"An error occurred: {str(error)}", 500

if __name__ == '__main__':
    app.run(debug=True)
