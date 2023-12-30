from flask import Flask, redirect, url_for, render_template, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from user import User
from post import Post
import hashlib
from bson import ObjectId
from flask import  session
from bson import ObjectId
from json import JSONEncoder
from bson import ObjectId
app = Flask(__name__)

app.secret_key = 'hi'

app.config['UPLOAD_FOLDER'] = 'static/images'

CORS(app)

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)

app.json_encoder = CustomJSONEncoder

@app.route("/")
def login1():
    return render_template("login.html")


@app.route("/edit.html")
def edit():
    return render_template("edit.html")


from flask import render_template

@app.route("/popup/<postID>")
def popup(postID):
    # Convert the string postID back to ObjectId
    postID = ObjectId(postID)
    
    post = Post()
    post.getPostByID(postID)
    
    imageURLs = post.getImages()
    Title = post.getTitle()
    loc=post.getLocation()
    des = post.getDescription()
    startPrice, endPrice = post.getStartPrice(), post.getEndPrice()
    user_id = session.get('user_id')
    result_user = User()
    result_user.getUserByID(user_id)
    username = result_user.getUserName()
    profile_image = result_user.getProfilePicture()
    
    
    return render_template(
        "popup.html",
        imageURLs=imageURLs,
        postID=postID,
        startPrice=startPrice,
        endPrice=endPrice,
        title=Title,
        des=des,
        loc=loc,profile_image=profile_image
    )

@app.route("/forget.html")
def forget():
    return render_template("forget.html")


@app.route("/about.html")
def about():
    user_id = session.get('user_id')
    result_user = User()
    result_user.getUserByID(user_id)
    username = result_user.getUserName()
    profile_image = result_user.getProfilePicture()
    
    return render_template("about.html",profile_image=profile_image)


@app.route("/categories.html")
def category():
    adventure_posts = getCategoryPost("Adventure")
    user_id = session.get('user_id')
    result_user = User()
    result_user.getUserByID(user_id)
    username = result_user.getUserName()
    profile_image = result_user.getProfilePicture()
    
    return render_template("categories.html", adventure_posts=adventure_posts,profile_image=profile_image)


@app.route("/arcade.html")
def arcade():
    Arcade_posts = getCategoryPost("Arcade")
    user_id = session.get('user_id')
    result_user = User()
    result_user.getUserByID(user_id)
    username = result_user.getUserName()
    profile_image = result_user.getProfilePicture()
    
    return render_template("arcade.html", Arcade_posts=Arcade_posts,profile_image=profile_image)


@app.route("/cinema.html")
def cinema():
    Cinema_posts = getCategoryPost("Cinema")
    user_id = session.get('user_id')
    result_user = User()
    result_user.getUserByID(user_id)
    username = result_user.getUserName()
    profile_image = result_user.getProfilePicture()
    
    return render_template("cinema.html", Cinema_posts=Cinema_posts,profile_image=profile_image)


@app.route("/food.html")
def food():
    Food_posts = getCategoryPost("Food")
    user_id = session.get('user_id')
    result_user = User()
    result_user.getUserByID(user_id)
    username = result_user.getUserName()
    profile_image = result_user.getProfilePicture()
   
    return render_template("food.html", Food_posts=Food_posts,profile_image=profile_image)


@app.route("/date.html")
def date():
    user_id = session.get('user_id')
    result_user = User()
    result_user.getUserByID(user_id)
    username = result_user.getUserName()
    profile_image = result_user.getProfilePicture()
    
    Dates_posts = getCategoryPost("Dates")
    return render_template("date.html", Dates_posts=Dates_posts,profile_image=profile_image)


@app.route("/place.html")
def place():
    user_id = session.get('user_id')
    result_user = User()
    result_user.getUserByID(user_id)
    username = result_user.getUserName()
    profile_image = result_user.getProfilePicture()
   
    return render_template("place.html",profile_image=profile_image)


@app.route("/like", methods=["POST"])
def like_image():
    if request.method == "POST":
        image_id = request.json.get("imageId")
        return "Liked"






@app.route("/home.html")
def home():
    adventure_posts = getCategoryPost("Adventure")
    Dates_posts = getCategoryPost("Dates")
    Food_posts = getCategoryPost("Food")
    Cinema_posts = getCategoryPost("Cinema")
    Arcade_posts = getCategoryPost("Arcade")
    user_id = session.get('user_id')
    result_user = User()
    result_user.getUserByID(user_id)
    username = result_user.getUserName()
    profile_image = result_user.getProfilePicture()

    
    if adventure_posts is None:
        adventure_posts = [] 
    return render_template(
        "/home.html",
        adventure_posts=adventure_posts,
        Dates_posts=Dates_posts,
        Food_posts=Food_posts,
        Cinema_posts=Cinema_posts,
        Arcade_posts=Arcade_posts,profile_image=profile_image
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
            file.save(
                os.path.join("static/images/", filename)
            )  # Save each file to the specified path
            results.append(filename)  # Store the filenames for response
    info = {
        "Title": Title,
        "Location": Location,
        "Description": Description,
        "StartPrice": range1,
        "EndPrice": range2,
        "Category": selectedCategory,  # Use lowercase 'category' here
    }

    post.createPost(results, info)  # Save data to MongoDB
    message="Place added successfully"
    return render_template("/place.html",message =message)

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

def changeProfilePicture(userID, imageName):
    user = User()
    user.getUserByID(userID)  # Use the existing user instance associated with the userID
    query = {"$set": {"ProfilePicture": imageName}}
    user.editData(query, userID)
    user.setProfilePicture(imageName)

@app.route("/update", methods=["POST"])
def update_profile():
    new_username = request.form.get("new_username")
    old_password = request.form.get("old_password")
    new_password = request.form.get("new_password")
    imageFiles = request.files.getlist("imageFiles")

    user = User()
    
    user_id = session.get('user_id')
    result_user = User()
    result_user.getUserByID(user_id)
    username = result_user.getUserName()
    profile_image = result_user.getProfilePicture()
    

   

    imageFiles = request.files.getlist("imageFiles")

    results = []
    if imageFiles:
        for file in imageFiles:
            filename = secure_filename(file.filename)
            file.save(os.path.join("static/images/", filename))
            # changeProfilePicture(user_id, filename)
            results.append(filename)
        

    for result_filename in results:
        changeProfilePicture(user_id, result_filename)
        profile_image = result_user.getProfilePicture()

   
    favorite_posts = result_user.getFavorite()
    fav = len(favorite_posts)
    if old_password is not None and old_password != "":  # Check if old_password is provided and not empty
        hashed_old_password = hashlib.sha256(old_password.encode()).hexdigest()
        print(hashed_old_password, user.getPassword())
        
        if hashed_old_password != user.getPassword():
            alert_message= "Old password incorrect. Please try again."
            return render_template(
        "/edit.html", alert_message=alert_message
    )

    
    if new_username is not None and new_username!="" :
        user.editData({"$set": {"Username": new_username}}, user_id)
        username=new_username

    if new_password is not None and old_password is not None and new_password != "" and old_password != "":  # Check both old and new passwords
        hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()
        
        if hashed_new_password == user.getPassword():
            alert_message= "New password must be different from the old password."
            return render_template(
        "/edit.html", alert_message=alert_message
    )


        user.editData({"$set": {"Password": hashed_new_password}}, user_id)

    alert_message= "Profile updated successfully!"
    return render_template(
        "/profile.html", alert_message=alert_message,username=username, profile_image=profile_image, fav=fav, favorite_posts=favorite_posts
    )


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
            alert_message = "User not found."
        elif user_id == "Wrong Password":
            alert_message = "Wrong password."
        else:
            alert_message = f"Login successful! User ID: {user_id}"
            session['user_id'] = user_id
            user_id = session.get('user_id')
            result_user = User()
            result_user.getUserByID(user_id)
            username = result_user.getUserName()
            profile_image = result_user.getProfilePicture()
            favorite_posts = result_user.getFavorite()
            fav = len(favorite_posts)
            return render_template(
                "/profile.html", username=username, profile_image=profile_image, fav=fav, favorite_posts=favorite_posts
            )

    return render_template(
        "/login.html", alert_message=alert_message, username=username
    )


from bson import ObjectId

@app.route("/signup", methods=["POST"])
def signup():
    alert_message = None
    username = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_id = SignUp(username, password)

        # Convert ObjectId to string
        user_id_str = str(user_id)
       

        alert_message = f"Signup successful! User ID: {user_id_str}"
        session['user_id'] = user_id_str
        user_id = session.get('user_id')
        result_user = User()
        result_user.getUserByID(user_id)
        username = result_user.getUserName()
        profile_image = result_user.getProfilePicture()
        favorite_posts = result_user.getFavorite()
        fav = len(favorite_posts)

    return render_template("/profile.html", username=username, profile_image=profile_image, fav=fav, favorite_posts=favorite_posts)


# login


# home
def getCategoryPost(categoryName):
    temp = Post()
    posts = temp.getPostsByCategory(categoryName)
    return posts





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
    user_id = session.get('user_id')
    result_user = User()
    result_user.getUserByID(user_id)
    username = result_user.getUserName()
    profile_image = result_user.getProfilePicture()
    favorite_posts = result_user.getFavorite()
    fav = len(favorite_posts)

    return render_template(
        "profile.html", username=username, profile_image=profile_image, fav=fav, favorite_posts=favorite_posts
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
