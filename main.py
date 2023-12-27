from flask import Flask, redirect, url_for, render_template, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/profile.html")
def profile():
    return render_template("profile.html")

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
    imageFiles = request.files.getlist("imageFiles")  # "imageFiles" should match the name attribute of your file input

    results = []
    for file in imageFiles:
        if file and isinstance(file.filename, str) and file.filename != "":
            filename = secure_filename(file.filename)
            file.save(os.path.join("static/images/", filename))  # Save each file to the specified path
            results.append(filename)  # Store the filenames for response

    result = calling_function(Title, imageFiles, Description, Location)
    return jsonify(result=result)


def calling_function(Title, imageFile, Description, Location):
    return(Title, Description, Location)
    if imageFile == {}:
        imageFile.save("static/images/" + imageFile.filename)

    else:
        return "kkkk"


if __name__ == "__main__":
    app.run(debug=True)
