from user import User


def getProfilePicture(userID):
    user = User()
    user.getUserByID(userID)
    return user.getProfilePicture()


# def getUserFavorite(userID):
#     user = User()
#     user.getUserByID(userID)
#     favorites = user.getFavorite()
#     favs = []
#     for fav in favorites:
#         post = Post()
#         favs.append(post.getPostFromID(post))
#     return favs
