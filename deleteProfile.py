from user import User


def removeProfilePicture(userID, imageName):
    user = User()
    imagePath = imageName
    query = {"$set": {"ProfilePicture": imagePath}}
    user.editData(query, userID)
    user.setProfilePicture(imagePath)
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
