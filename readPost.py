from post import Post


def getCategoryPost(categoryName):
    temp = Post()
    posts = temp.getPostsByCategory(categoryName)
    return posts


def readPost(postID):
    post = Post()
    post.getPostByID(postID)
    return post
