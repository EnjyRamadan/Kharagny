from flask import Flask, redirect, url_for, render_template, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/categories.html")
def category():
    return render_template("categories.html")

@app.route("/place.html")
def place():
    return render_template("categories.html")




if __name__ == "__main__":
    app.run(debug=True)
