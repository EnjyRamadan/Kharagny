from user import User


def putProfilePicture(userID, imagePath):
    user = User()
    user.putProfilePicture(userID, imagePath)
