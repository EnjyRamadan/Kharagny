from user import User
import hashlib
from bson import Binary


def changeProfilePicture(userID, imageName):
    user = User()
    imagePath = "static/images/" + imageName
    with open(imagePath, "rb") as file:
        imageData = file.read()
        binaryData = Binary(imageData)
    query = {"$set": {"profilePicture": binaryData}}
    user.editData(query, userID)
    user.setProfilePicture(binaryData)


def changeUserName(userID, newUserName):
    user = User()
    query = {"$set": {"userName": newUserName}}
    user.editData(query, userID)
    user.setUserName(newUserName)


def changePassword(userID, newPassword, oldPassword):
    user = User()
    user.getUserByID(userID)
    hashedPassword = hashlib.sha256(oldPassword.encode()).hexdigest()
    if hashedPassword == user.getPassword():
        query = {"$set": {"password": newPassword}}
        user.editData(query, userID)
        user.setPassword(newPassword)


def addFavorite(userID, post):
    pass


def deleteFavorite(userID, post):
    pass
