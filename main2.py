from flask import Flask, redirect, url_for, render_template, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from user import User
from post import Post

app = Flask(__name__)
CORS(app)


@app.route("/")
def login1():
    return render_template("login.html")


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
    adventure_posts = getCategoryPost("Adventure")
    return render_template("categories.html", adventure_posts=adventure_posts)


@app.route("/arcade.html")
def arcade():
    Arcade_posts = getCategoryPost("Arcade")
    return render_template("arcade.html", Arcade_posts=Arcade_posts)


@app.route("/cinema.html")
def cinema():
    Cinema_posts = getCategoryPost("Cinema")
    return render_template("cinema.html", Cinema_posts=Cinema_posts)


@app.route("/food.html")
def food():
    Food_posts = getCategoryPost("Food")
    return render_template("food.html", Food_posts=Food_posts)


@app.route("/date.html")
def date():
    Dates_posts = getCategoryPost("Dates")
    return render_template("date.html", Dates_posts=Dates_posts)


@app.route("/place.html")
def place():
    return render_template("place.html")


@app.route("/call_function", methods=["POST"])
def call_function():
    post = Post()
    Title = request.form.get("Title")

    Location = request.form.get("Location")

    Description = request.form.get("Description")

    range1 = request.form.get("range1")
    range2 = request.form.get("range2")

    selectedCategory = request.form.get("category")

    imageFiles = request.files.getlist("imageFiles")

    results = []
    if imageFiles:
        for file in imageFiles:
            filename = secure_filename(file.filename)
            file.save(
                os.path.join("static/images/", filename)
            )  # Save each file to the specified path
            results.append(filename)  # Store the filenames for response
    info = {
        "Title": Title,
        "Location": Location,
        "Description": Description,
        "range1": range1,
        "range2": range2,
        "category": selectedCategory,  # Use lowercase 'category' here
    }

    post.createPost(results, info)  # Save data to MongoDB
    return render_template("home.html")


def calling_function(Title, imageFile, Description, Location, range1, range2, category):
    return (Title, Description, Location, imageFile, range1, range2, category)
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
    username = None

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
            return render_template(
                "/profile.html", alert_message=alert_message, username=username
            )

    return render_template(
        "/login.html", alert_message=alert_message, username=username
    )


@app.route("/signup", methods=["POST"])
def signup():
    alert_message = None
    username = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_id = SignUp(username, password)
        alert_message = f"Signup successful! User ID: {user_id}"

    return render_template(
        "/profile.html", alert_message=alert_message, username=username
    )


# login


# home
def getCategoryPost(categoryName):
    temp = Post()
    posts = temp.getPostsByCategory(categoryName)
    return posts


@app.route("/home.html")
def home():
    adventure_posts = getCategoryPost("Adventure")
    Dates_posts = getCategoryPost("Dates")
    Food_posts = getCategoryPost("Food")
    Cinema_posts = getCategoryPost("Cinema")
    Arcade_posts = getCategoryPost("Arcade")

    return render_template(
        "/home.html",
        adventure_posts=adventure_posts,
        Dates_posts=Dates_posts,
        Food_posts=Food_posts,
        Cinema_posts=Cinema_posts,
        Arcade_posts=Arcade_posts,
    )
    return render_template("home.html")


# Replace this with your database logic to fetch data
def get_data_from_database():
    # Simulated data, replace this with your database logic
    image_urls = ["image1.jpg", "image2.jpg", "image3.jpg"]
    post_id = 123  # Replace this with the actual post ID
    return image_urls, post_id


@app.route("/popup/<postID>")
def popup(postID):
    # Get data from the database
    image_urls, post_id = get_data_from_database()

    # Pass data to the template
    return render_template("popup.html", image_urls=image_urls, post_id=post_id)


@app.route("/addToFavorites/<user_id>/<post_id>", methods=["POST"])
def addToFavorites(user_id, post_id):
    if request.is_json:
        data = request.get_json()
        addPostToFavorite(user_id, post_id)
        return jsonify({"success": True}), 200
    else:
        return jsonify({"error": "Invalid request data"}), 400


def addPostToFavorite(ID, postID):
    user = User
    user.getUserByID(ID)
    user.addToFavorite(postID)


# home

if __name__ == "__main__":
    app.run(debug=True)
