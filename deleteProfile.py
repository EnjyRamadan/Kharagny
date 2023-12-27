from user import User
from bson import Binary


def deleteAccount(ID):
    user = User
    user.getUserByID(ID)
    user.deleteAccount()


def removeProfilePicture(ID):
    user = User
    with open("static/images/defaultProfilePicture.jpg", "rb") as file:
        image_data = file.read()
    binaryData = Binary(image_data)
    query = {
        "$set": {
            "profilePicture": binaryData,
        }
    }
    user.editData(query, ID)


# _id = None
# _userName = None
# _password = None
# _favorite = []
# _profilePicture = None


def removeFromFavorite(ID, postID):
    user = User
    user.getUserByID(ID)
    