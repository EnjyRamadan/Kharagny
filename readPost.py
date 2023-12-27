from post import Post


def getCategoryPost(categoryName):
    temp = Post()
    temp.getAllPostsForCategory(categoryName)
    
