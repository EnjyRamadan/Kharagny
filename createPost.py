from post import Post
from user import User


def addNewPost(data, userID):
    user = User()
    user.getUserByID(userID)
    post = Post()
    image = data["Images"]
    del data["Images"]
    post.createPost(image, data)
    user.addPost(post.getID())
    return post
