from user import User
from io import BytesIO
from PIL import Image
import json

def getProfilePicture(userID):
    user = User()
    user.getUserByID(userID)
    image_path = BytesIO(user.getProfilePicture())
    data = {"imagePath": image_path}
    json_data = json.dumps(data)
    return json_data


# def getUserFavorite(userID):
#     user = User()
#     user.getUserByID(userID)
#     favorites = user.getFavorite()
#     favs = []
#     for fav in favorites:
#         post = Post()
#         favs.append(post.getPostFromID(post))
#     return favs
