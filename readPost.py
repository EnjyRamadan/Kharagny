from post import Post


def getCategoryPost(categoryName):
    temp = Post()
    posts = temp.getAllPostsForCategory(categoryName)
    return posts


def readPost(postID):
    post = Post()
