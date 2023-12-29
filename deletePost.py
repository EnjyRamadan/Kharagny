from post import Post


def removeImageFromPost(postID, imagePath):
    post = Post()
    post.removeFromImages(postID, imagePath)


def removePost():
    post = Post
    post.deletePost()
