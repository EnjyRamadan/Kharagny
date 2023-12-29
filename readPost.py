from post import Post


def getCategoryPost(categoryName):
    temp = Post()
    posts = temp.getPostsByCategory(categoryName)
    for post in posts:
        imagesPath = []
        for image in post.getImages():
            imagesPath.append(image)
            print(image)
        post.setImages(imagesPath)
    return posts


def readPost(postID):
    post = Post()
    post.getPostByID(postID)
    return post
