from flask import Flask, redirect, url_for, render_template, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from user import User
from post import Post
import hashlib

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
CORS(app)


@app.route("/")
def login1():
    return render_template("login.html")


@app.route("/edit.html")
def edit():
    return render_template("edit.html")


@app.route("/popup.html/<postID>")
def popup(postID):
    post = Post
    post.getPostByID(postID)
    imageURLs = post.getImages()
    Title = post.getTitle()
    des = post.getDescription()
    startPrice, endPrice = post.getStartPrice(), post.getEndPrice()
    return render_template(
        "popup.html",
        imageURLs=imageURLs,
        postID=postID,
        startPrice=startPrice,
        endPrice=endPrice,
        title=Title,
        des=des,
    )


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


@app.route("/like", methods=["POST"])
def like_image():
    if request.method == "POST":
        image_id = request.json.get("imageId")
        return "Liked"


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

    # Title, Description, Location,imageFile,range1,range2,strategy = calling_function(Title, imageFiles, Description, Location, range1, range2,selectedCategory)
    # return jsonify(Title=Title, Description=Description, Location=Location,imageFile=imageFile,range1=range1,range2=range2,strategy=strategy)


def calling_function(Title, imageFile, Description, Location, range1, range2, category):
    return (Title, Description, Location, imageFile, range1, range2, category)
    if imageFile == {}:
        imageFile.save("static/images/" + imageFile.filename)

    else:
        return "kkkk"


def edit_profile():
    return render_template("edit.html")


@app.route("/update", methods=["POST"])
def update_profile():
    new_username = request.form["new_username"]
    old_password = request.form["old_password"]
    new_password = request.form["new_password"]
    email = request.form["email"]
    user = User()
    document = user.getFieldFromUser({"Username": new_username}, {"Password": 1})
    user_id = document[0]["_id"]
    user.getUserByID(user_id)
    hashedPassword = hashlib.sha256(old_password.encode()).hexdigest()
    print(hashedPassword, user.getPassword())
    if hashedPassword != user.getPassword():
        return "Old password incorrect. Please try again."

    if new_username:
        user.editData({"$set": {"Username": new_username}}, user_id)

    if new_password:
        hashedPassword = hashlib.sha256(new_password.encode()).hexdigest()
        user.editData({"$set": {"Password": hashedPassword}}, user_id)

    return "Profile updated successfully!"


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
            session["user_id"] = str(user_id)
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
        session["user_id"] = str(user_id)
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


# home
# favourites
from user import User
from post import Post


def getUserFavorite(userID):
    user = User()
    user.getUserByID(userID)
    favorites = user.getField()
    favs = []
    for fav in favorites:
        post = Post()
        favs.append(post.getPostFromID())
    return favs


@app.route("/profile.html")
def profile():
    # Use the user_id to fetch user information
    user_instance = User()
    user_id = user_instance.getID()
    user_instance.getUserByID(user_id)
    # Get user information
    name2 = user_instance.getUserName()
    favorite_posts = getUserFavorite(user_id)
    return render_template(
        "profile.html",
        favorite_posts=favorite_posts,
        name2=name2,
        num_favorite_posts=len(favorite_posts),
    )


if __name__ == "__main__":
    app.run(debug=True)
