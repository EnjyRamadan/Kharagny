from user import User
from bson import Binary


def removeProfilePicture(userID, imageName):
    user = User()
    imagePath = "static/images/" + imageName
    with open(imagePath, "rb") as file:
        imageData = file.read()
        binaryData = Binary(imageData)
    query = {"$set": {"ProfilePicture": binaryData}}
    user.editData(query, userID)
    user.setProfilePicture(binaryData)
    return user


def removePostFromFavorite(ID, postID):
    user = User
    user.getUserByID(ID)
    user.removeFromFavorite(postID)
    return user


def deleteProfile(ID):
    user = User
    user.getUserByID(ID)
    user.deleteAccount()
