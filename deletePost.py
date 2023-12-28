from post import Post


def removeImageFromPost(postID, imagePath):
    post = Post()
    post.removeFromImages(postID, imagePath)
from post import Post

# Example input
imagesPath = [
    "download.jpg",
    "sawsan2.jpg",
]  # Replace these with actual image file names
info = {
    "category": "Adventure",
    "title": "Amazing Sale",
    "location": "City Center",
    "desc": "Sale on various items",
    "StartPrice": 50,
    "EndPrice": 100,
}

# Call the createPost method
post = Post()  # Assuming Post is the class where createPost is defined
post.createPost(imagesPath, info)