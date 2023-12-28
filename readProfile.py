from user import User
from post import Post


def getProfilePicture(userID):
    user = User()
    user.getUserByID(userID)
    return user.getProfilePicture()


def getUserFavorite(userID):
    user = User()
    user.getUserByID(userID)
    favorites = user.getField()
    favs = []
    for fav in favorites:
        post = Post()
        favs.append(post.getPostFromID())
    return favs
