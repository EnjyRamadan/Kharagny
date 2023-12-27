from user import User
from io import BytesIO
from PIL import Image


def getProfilePicture(userID):
    user = User()
    user.getUserByID(userID)
    return Image.open(BytesIO(user.getProfilePicture()))


# def getUserFavorite(userID):
#     user = User()
#     user.getUserByID(userID)
#     favorites = user.getFavorite()
#     favs = []
#     for fav in favorites:
#         post = Post()
#         favs.append(post.getPostFromID(post))
#     return favs
