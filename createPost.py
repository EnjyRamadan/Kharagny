from post import Post


def addNewPost(data):
    post = Post
    image = data["Images"]
    del data["Images"]
    post.createPost(image, data)
    return post
