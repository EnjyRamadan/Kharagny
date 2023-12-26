from flask import Flask, redirect, url_for, render_template, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/profile.html")
def about():
    return render_template("profile.html")


@app.route("/categories.html")
def category():
    return render_template("categories.html")


@app.route("/place.html")
def place():
    return render_template("place.html")


@app.route("/call_function", methods=["POST"])
def call_function():
    data = request.get_json()
    Title = data.get("Title")

    imageFile = data.get("imageFile")

    Description = data.get("Description")
    Location = data.get("Location")

    result = calling_function(Title, imageFile, Description, Location)
    return jsonify(result=result)


def calling_function(Title, imageFile, Description, Location):
    # return(imageFile)
    if imageFile == {}:
        imageFile.save("static/images/" + imageFile.filename)

    else:
        return "kkkk"


if __name__ == "__main__":
    app.run(debug=True)
