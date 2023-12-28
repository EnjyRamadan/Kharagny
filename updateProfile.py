from user import User
import hashlib


def changeProfilePicture(userID, imageName):
    user = User()
    imagePath = "static/images/" + imageName
    query = {"$set": {"ProfilePicture": imagePath}}
    user.editData(query, userID)
    user.setProfilePicture(imagePath)


def changeUserName(userID, newUserName):
    user = User()
    query = {"$set": {"Username": newUserName}}
    user.editData(query, userID)
    user.setUserName(newUserName)


def changePassword(userID, newPassword, oldPassword):
    user = User()
    user.getUserByID(userID)
    hashedPassword = hashlib.sha256(oldPassword.encode()).hexdigest()
    if hashedPassword == user.getPassword():
        query = {"$set": {"Password": newPassword}}
        user.editData(query, userID)
        user.setPassword(newPassword)


def addPostToFavorite(ID, postID):
    user = User
    user.getUserByID(ID)
    user.addToFavorite(postID)
