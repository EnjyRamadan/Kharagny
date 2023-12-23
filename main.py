from flask import Flask, redirect, url_for, render_template, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/vis.html")
def graph():
    return render_template("vis.html")
@app.route("/about.html")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)
