from user import User
from io import BytesIO
from PIL import Image


def getProfilePicture(userID):
    user = User()
    user.getUserByID(userID)
    return Image.open(BytesIO(user.getProfilePicture()))
