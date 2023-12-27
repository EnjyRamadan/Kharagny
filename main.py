from flask import Flask, redirect, url_for, render_template, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from user import User

app = Flask(__name__)
CORS(app)


@app.route("/")
def login1():
    return render_template("login.html")


@app.route("/home.html")
def home():
    return render_template("home.html")


@app.route("/profile.html")
def profile():
    return render_template("profile.html")


@app.route("/edit.html")
def edit():
    return render_template("edit.html")


@app.route("/popup.html")
def pop():
    return render_template("popup.html")


@app.route("/forget.html")
def forget():
    return render_template("forget.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/categories.html")
def category():
    return render_template("categories.html")


@app.route("/arcade.html")
def arcade():
    return render_template("arcade.html")


@app.route("/cinema.html")
def cinema():
    return render_template("cinema.html")


@app.route("/food.html")
def food():
    return render_template("food.html")


@app.route("/date.html")
def date():
    return render_template("date.html")


@app.route("/place.html")
def place():
    return render_template("place.html")


@app.route("/call_function", methods=["POST"])
def call_function():
    Title = request.form["Title"]
    Description = request.form["Description"]
    Location = request.form["Location"]
    range1 = request.form["range1"]
    range2 = request.form["range2"]
    imageFiles = request.files.getlist(
        "imageFiles"
    )  # "imageFiles" should match the name attribute of your file input

    results = []
    for file in imageFiles:
        if file and isinstance(file.filename, str) and file.filename != "":
            filename = secure_filename(file.filename)
            file.save(
                os.path.join("static/images/", filename)
            )  # Save each file to the specified path
            results.append(filename)  # Store the filenames for response

    result = calling_function(Title, imageFiles, Description, Location, range1, range2)
    return jsonify(result=result)


def calling_function(Title, imageFile, Description, Location, range1, range2):
    return (Title, Description, Location)
    if imageFile == {}:
        imageFile.save("static/images/" + imageFile.filename)

    else:
        return "kkkk"


# login


def Login(userName, password):
    temp = User()
    respond = temp.Login(userName, password)
    if respond == True:
        return temp.getID()
    else:
        return respond


def SignUp(userName, password):
    temp = User()
    _id = temp.SignUp(userName, password)
    return _id


@app.route("/login", methods=["POST"])
def login():
    alert_message = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_id = Login(username, password)

        if user_id == "User Not Found":
            alert_message = "Login failed! User not found."
        elif user_id == "Wrong Password":
            alert_message = "Login failed! Wrong password."
        else:
            alert_message = f"Login successful! User ID: {user_id}"

    return render_template("login.html", alert_message=alert_message)


@app.route("/signup", methods=["POST"])
def signup():
    alert_message = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_id = SignUp(username, password)
        alert_message = f"Signup successful! User ID: {user_id}"

    return render_template("signup.html", alert_message=alert_message)


# login


if __name__ == "__main__":
    app.run(debug=True)
