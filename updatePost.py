from post import Post


def changeDescription(postID, newDisc):
    post = Post()
    post.getPostByID(postID)
    query = {"$set": {"Description": newDisc}}
    post.setDescription(newDisc)
    post.editData(query, postID)


def changeLocation(postID, newLoc):
    post = Post()
    post.getPostByID(postID)
    query = {"$set": {"Location": newLoc}}
    post.setLocation(newLoc)
    post.editData(query, postID)


def changeTitle(postID, newTitle):
    post = Post()
    post.getPostByID(postID)
    query = {"$set": {"Title": newTitle}}
    post.setTitle(newTitle)
    post.editData(query, postID)


def changeTitle(postID, newTitle):
    post = Post()
    post.getPostByID(postID)
    query = {"$set": {"Title": newTitle}}
    post.setTitle(newTitle)
    post.editData(query, postID)


def changePriceRange(postID, newStart, newEnd):
    post = Post()
    post.getPostByID(postID)
    query = {"$set": {"StartPrice": newStart, "EndPrice": newEnd}}
    post.setStartPrice(newStart)
    post.setEndPrice(newEnd)
    post.editData(query, postID)


def addImageToPost(postID, imagePath):
    post = Post()
    post.getPostByID(postID)
    query = {"$push": {"Images": imagePath}}
    
