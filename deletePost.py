from post import Post


def removeImageFromPost(postID, imagePath):
    post = Post()
    post.removeFromImages(postID, imagePath)

