from flask import Flask, redirect, url_for, render_template, jsonify, request, session
from werkzeug.utils import secure_filename
from json import JSONEncoder
from flask_cors import CORS
from bson import ObjectId
from user import User
from post import Post
import hashlib
import os

app = Flask(__name__)
app.secret_key = "hi"
CORS(app)


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)


app.json_encoder = CustomJSONEncoder


def getFavoritePost(posts):
    accPost = []
    for post in posts:
        accPost.append(readPost(post))
    return accPost


@app.route("/")
def login1():
    return render_template("login.html")


@app.route("/edit.html")
def edit():
    return render_template("edit.html")


def getUserData(userID):
    result_user = User()
    result_user.getUserByID(userID)
    username = result_user.getUserName()
    profile_image = result_user.getProfilePicture()
    return username, profile_image


@app.route("/popup/<postID>")
def popup(postID):
    postID = ObjectId(postID)
    post = Post()
    post.getPostByID(postID)
    imageURLs = post.getImages()
    Title = post.getTitle()
    loc = post.getLocation()
    des = post.getDescription()
    startPrice, endPrice = post.getStartPrice(), post.getEndPrice()
    user_id = session.get("user_id")
    result_user = User()
    result_user.getUserByID(user_id)
    username = result_user.getUserName()
    profile_image = result_user.getProfilePicture()
    favorite_posts = result_user.getFavorite()
    is_in_favorites = str(postID) in favorite_posts
    return render_template(
        "popup.html",
        imageURLs=imageURLs,
        postID=postID,
        startPrice=startPrice,
        endPrice=endPrice,
        title=Title,
        des=des,
        loc=loc,
        profile_image=profile_image,
        isInFavorites=is_in_favorites,
    )


@app.route("/forget.html")
def forget():
    return render_template("forget.html")


@app.route("/about.html")
def about():
    user_id = session.get("user_id")
    username, profile_image = getUserData(user_id)
    return render_template("about.html", profile_image=profile_image)


@app.route("/categories.html")
def category():
    adventure_posts = getCategoryPost("Adventure")
    user_id = session.get("user_id")
    username, profile_image = getUserData(user_id)
    return render_template(
        "categories.html", adventure_posts=adventure_posts, profile_image=profile_image
    )


@app.route("/arcade.html")
def arcade():
    Arcade_posts = getCategoryPost("Arcade")
    user_id = session.get("user_id")
    username, profile_image = getUserData(user_id)
    return render_template(
        "arcade.html", Arcade_posts=Arcade_posts, profile_image=profile_image
    )


@app.route("/cinema.html")
def cinema():
    Cinema_posts = getCategoryPost("Cinema")
    user_id = session.get("user_id")
    username, profile_image = getUserData(user_id)
    return render_template(
        "cinema.html", Cinema_posts=Cinema_posts, profile_image=profile_image
    )


@app.route("/food.html")
def food():
    Food_posts = getCategoryPost("Food")
    user_id = session.get("user_id")
    username, profile_image = getUserData(user_id)
    return render_template(
        "food.html", Food_posts=Food_posts, profile_image=profile_image
    )


@app.route("/date.html")
def date():
    Dates_posts = getCategoryPost("Dates")
    user_id = session.get("user_id")
    username, profile_image = getUserData(user_id)
    return render_template(
        "date.html", Dates_posts=Dates_posts, profile_image=profile_image
    )


@app.route("/place.html")
def place():
    user_id = session.get("user_id")
    username, profile_image = getUserData(user_id)
    return render_template("place.html", profile_image=profile_image)


def addPostToFavorite(ID, postID):
    user = User()
    user.getUserByID(ID=ID)
    user.addToFavorite(postID)


def removePostFromFavorite(ID, postID):
    user = User()
    user.getUserByID(ID)
    user.removeFromFavorite(postID)
    return user


@app.route("/like/<postID>", methods=["POST"])
def like_post(postID):
    user = User()
    userID = session.get("user_id")
    user.getUserByID(userID)
    fav = user.getFavorite()
    isInFavorites = str(postID) in fav
    print(isInFavorites)
    if isInFavorites:
        removePostFromFavorite(userID, postID)
    else:
        addPostToFavorite(userID, postID)
    return jsonify({"message": "Post liked successfully"})


@app.route("/home.html")
def home():
    adventure_posts = getCategoryPost("Adventure")
    Dates_posts = getCategoryPost("Dates")
    Food_posts = getCategoryPost("Food")
    Cinema_posts = getCategoryPost("Cinema")
    Arcade_posts = getCategoryPost("Arcade")
    user_id = session.get("user_id")
    username, profile_image = getUserData(user_id)
    return render_template(
        "/home.html",
        adventure_posts=adventure_posts,
        Dates_posts=Dates_posts,
        Food_posts=Food_posts,
        Cinema_posts=Cinema_posts,
        Arcade_posts=Arcade_posts,
        profile_image=profile_image,
    )


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
            file.save(os.path.join("static/images/", filename))
            results.append(filename)
    info = {
        "Title": Title,
        "Location": Location,
        "Description": Description,
        "StartPrice": range1,
        "EndPrice": range2,
        "Category": selectedCategory,
    }
    post.createPost(results, info)
    message = "Place added successfully"
    return render_template("/place.html", message=message)


def calling_function(Title, imageFile, Description, Location, range1, range2, category):
    return (Title, Description, Location, imageFile, range1, range2, category)


def edit_profile():
    return render_template("edit.html")


@app.route("/update", methods=["POST"])
def update_profile():
    new_username = request.form["new_username"]
    old_password = request.form["old_password"]
    new_password = request.form["new_password"]
    user = User()
    document = user.getFieldFromUser(
        {"Username": new_username}, {"Password": 1, "_id": 1}
    )
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
            alert_message = "User not found."
        elif user_id == "Wrong Password":
            alert_message = "Wrong password."
        else:
            alert_message = f"Login successful! User ID: {user_id}"
            session["user_id"] = user_id
            user_id = session.get("user_id")
            result_user = User()
            result_user.getUserByID(user_id)
            username = result_user.getUserName()
            profile_image = result_user.getProfilePicture()
            favorite_posts = result_user.getFavorite()
            fav = len(favorite_posts)
            favorite_posts = getFavoritePost(favorite_posts)
            return render_template(
                "/profile.html",
                username=username,
                profile_image=profile_image,
                fav=fav,
                favorite_posts=favorite_posts,
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
        user_id_str = str(user_id)
        user_id = session.get("user_id")
        result_user = User()
        result_user.getUserByID(user_id)
        username = result_user.getUserName()
        profile_image = result_user.getProfilePicture()
        favorite_posts = result_user.getFavorite()
        fav = len(favorite_posts)
        favorite_posts = getFavoritePost(favorite_posts)
        alert_message = f"Signup successful! User ID: {user_id_str}"
        session["user_id"] = user_id_str
    return render_template(
        "/profile.html",
        username=username,
        profile_image=profile_image,
        fav=fav,
        favorite_posts=favorite_posts,
    )


def getCategoryPost(categoryName):
    temp = Post()
    posts = temp.getPostsByCategory(categoryName)
    return posts


def getUserFavorite(userID):
    user = User()
    user.getUserByID(userID)
    favorites = user.getField()
    favs = []
    for fav in favorites:
        post = Post()
        favs.append(post.getPostFromID())
    return favs


def readPost(postID):
    post = Post()
    post.getPostByID(postID)
    return post


@app.route("/profile.html")
def profile():
    user_id = session.get("user_id")
    result_user = User()
    result_user.getUserByID(user_id)
    username = result_user.getUserName()
    profile_image = result_user.getProfilePicture()
    favorite_posts = result_user.getFavorite()
    fav = len(favorite_posts)
    favorite_posts = getFavoritePost(favorite_posts)
    return render_template(
        "profile.html",
        username=username,
        profile_image=profile_image,
        fav=fav,
        favorite_posts=favorite_posts,
    )


def removeProfilePicture(userID, imageName):
    user = User()
    imagePath = "static/images/" + imageName
    query = {"$set": {"ProfilePicture": imagePath}}
    user.editData(query, userID)
    user.setProfilePicture(imagePath)
    return user


@app.route("/call_function2")
def remove():
    user = User()
    username = request.args.get("username")
    document = user.getFieldFromUser({"Username": username}, {"_id": 1})
    user_id = document[0]["_id"]
    string_id = str(user_id)
    user.getUserByID(string_id)
    image = user.getProfilePicture()
    removeProfilePicture(string_id, image)


if __name__ == "__main__":
    app.run(debug=True)
