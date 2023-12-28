from post import Post
from io import BytesIO
from PIL import Image

def getCategoryPost(categoryName):
    temp = Post()
    posts = temp.getPostsByCategory(categoryName)
    for post in posts:
        images = []
        for image in post.getImages():
            images.append(BytesIO(image))
            Image.open(image)
        post.setImages(images)

    return posts


def readPost(postID):
    post = Post()
    post.getPostByID(postID)
    return post
