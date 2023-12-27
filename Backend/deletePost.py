from post import Post


def removeImageFromPost(postID, imagePath):
    post = Post()
    post.getPostByID(postID)
    query = {"$pull": {"Images": imagePath}}
    images = post.getImages()
    images.remove(imagePath)
    post.setImages(images)
    post.editData(query, postID)
