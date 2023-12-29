from post import Post


def changeDescription(postID, newDisc):
    post = Post()
    post.getPostByID(postID)
    query = {"$set": {"Description": newDisc}}
    post.setDescription(newDisc)
    post.editData(query, postID)
    return post


def changeLocation(postID, newLoc):
    post = Post()
    post.getPostByID(postID)
    query = {"$set": {"Location": newLoc}}
    post.setLocation(newLoc)
    post.editData(query, postID)
    return post


def changeTitle(postID, newTitle):
    post = Post()
    post.getPostByID(postID)
    query = {"$set": {"Title": newTitle}}
    post.setTitle(newTitle)
    post.editData(query, postID)
    return post


def changeCategory(postID, newCategory):
    post = Post()
    post.getPostByID(postID)
    query = {"$set": {"Category": newCategory}}
    post.setCategory(newCategory)
    post.editData(query, postID)
    return post


def changePriceRange(postID, newStart, newEnd):
    post = Post()
    post.getPostByID(postID)
    query = {"$set": {"StartPrice": newStart, "EndPrice": newEnd}}
    post.setStartPrice(newStart)
    post.setEndPrice(newEnd)
    post.editData(query, postID)
    return post


def addImageToPost(postID, imageName):
    post = Post()
    post.addToImages(postID, imageName)
    return post
