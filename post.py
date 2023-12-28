from db import Database
from bson import Binary


class Post:
    def __init__(self):
        self._id = None
        self.images = []
        self.title = None
        self.location = None
        self.desc = None
        self.startPrice = None
        self.endPrice = None
        self.category = None

    def setID(self, ID):
        self._id = ID

    def getID(self):
        return self._id

    def setCategory(self, category):
        self.category = category

    def getCategory(self):
        return self.category

    def setStartPrice(self, price):
        self.startPrice = price

    def getStartPrice(self):
        return self.startPrice

    def setEndPrice(self, price):
        self.endPrice = price

    def getEndPrice(self):
        return self.endPrice

    def setImages(self, imageData):
        self.images = imageData

    def getImages(self):
        return self.images

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setLocation(self, location):
        self.location = location

    def getLocation(self):
        return self.location

    def setDescription(self, desc):
        self.desc = desc

    def getDescription(self):
        return self.desc

    def createPost(self, imagesPath, info):
        data = {
            "Images": imagesPath,
            "Title": info["Title"],
            "Category": info["category"],
            "Location": info["Location"],
            "Description": info["Description"],
            "StartPrice": info["range1"],
            "EndPrice": info["range2"],
        }
        self.setID(Database().Insert("Post", data))
        self.setCategory(info["category"])  # Use lowercase 'category'

        self.setDescription(info["Description"])
        self.setImages(imagesPath)
        self.setLocation(info["Location"])
        self.setTitle(info["Title"])
        self.setStartPrice(info["range1"])
        self.setEndPrice(info["range2"])

    def getPostByID(self, ID):
        result = Database().SelectByID("Post", ID)
        if result:
            self.setDescription(result["Description"])
            self.setCategory(result["Category"])
            self.setImages(result["Images"])
            self.setLocation(result["Location"])
            self.setTitle(result["Title"])
            self.setStartPrice(result["StartPrice"])
            self.setEndPrice(result["EndPrice"])

    def editData(self, query, ID):
        Database().UpdateOne("User", ID, query)

    def addToImages(self, ID, imagePath):
        images = self.getImages()
        images.append(imagePath)
        self.setImages(images)
        data = {"Images": imagePath}
        Database().AddToRecord("Post", ID, data)

    def removeFromImages(self, ID, imagePath):
        images = self.getImages()
        images.remove(imagePath)
        self.setImages(images)
        data = {"Images": imagePath}
        Database().RemoveFromRecord("Post", ID, data)

    def getPostsByCategory(self, categoryName):
        data = Database().SelectRecordCollection(
            "Post", {"Category": categoryName}, None
        )
        posts = []
        for record in data:
            post = Post()
            post.setID(record["_id"])
            post.setTitle(record["Title"])
            post.setImages(record["Images"])
            post.setEndPrice(record["EndPrice"])
            post.setCategory(record["Category"])
            post.setLocation(record["Location"])
            post.setStartPrice(record["StartPrice"])
            post.setDescription(record["Description"])
            posts.append(post)
        return posts
