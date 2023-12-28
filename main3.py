from flask import Flask, redirect, url_for, render_template, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from user import User
from post import Post
import createPost
import hashlib

app = Flask(__name__)
CORS(app)


@app.route("/")
def login1():
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
    adventure_posts = getCategoryPost("Adventure")
    return render_template("categories.html",adventure_posts=adventure_posts)


@app.route("/arcade.html")
def arcade():
    Arcade_posts = getCategoryPost("Arcade")
    return render_template("arcade.html",Arcade_posts = Arcade_posts )


@app.route("/cinema.html")
def cinema():
    Cinema_posts = getCategoryPost("Cinema")
    return render_template("cinema.html",Cinema_posts=Cinema_posts)


@app.route("/food.html")
def food():
    Food_posts = getCategoryPost("Food") 
    return render_template("food.html",Food_posts=Food_posts)


@app.route("/date.html")
def date():
    Dates_posts = getCategoryPost("Dates")
    return render_template("date.html",Dates_posts=Dates_posts)


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
    selectedCategory = request.form["category"]
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


#favorite

@app.route('/like', methods=['POST'])
def like_image():
    if request.method == 'POST':
        image_id = request.json.get('imageId')  # Get the imageId from the request

        # Perform your database operations here (e.g., insert or remove from the database)
        # Insert or remove 'image_id' from the database based on your logic

        # Return a success status
        return 'Liked'  # Or any success message you prefer




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


## update
def edit_profile():
    return render_template('edit.html')

@app.route('/update', methods=['POST'])
def update_profile():
    # Retrieve form data
    new_username = request.form['new_username']
    old_password = request.form['old_password']
    new_password = request.form['new_password']
    email = request.form['email']
    
    document =  user.getFieldFromUser({"username":  new_username})
    user_id = document['user_id']  # Replace with the actual user ID
    user = User()  # Assuming User is a class handling database operations
    
    # Check if old password matches
    user_data = user.getUserByID(user_id)
    hashed_old_password = hashlib.sha256(old_password.encode()).hexdigest()
    if hashed_old_password != user_data['password']:
        return "Old password incorrect. Please try again."
    
    # Update username if provided
    if new_username:
        user.editData({"$set": {"username": new_username}}, user_id)
        # user.setUserName(new_username)  # Set username in the user object if needed
    
    # Update password if provided
    if new_password:
        hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()
        user.editData({"$set": {"password": hashed_new_password}}, user_id)
        # user.setPassword(hashed_new_password)  # Set password in the user object if needed
    
    
    return "Profile updated successfully!"


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
        Arcade_posts=Arcade_posts

    )
    return render_template("home.html")


# home

if __name__ == "__main__":
    app.run(debug=True)