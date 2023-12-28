from post import Post


def addNewPost(data):
    post = Post
    info = data[:]
    del info["images"]
    post.createPost(data["images"], info)
    return post
