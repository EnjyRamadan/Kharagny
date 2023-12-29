from post import Post


def addNewPost(data):
    post = Post
    info = data[:]
    del info["Images"]
    post.createPost(data["Images"], info)
    return post
