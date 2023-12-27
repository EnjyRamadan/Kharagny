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

    def setID(self, ID):
        self._id = ID

    def getID(self):
        return self._id

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
        binaryData = []
        for imageData in imagesPath:
            with open("static/images/defaultProfilePicture.jpg", "rb") as file:
                imageData = file.read()
                binaryData.append(Binary(imageData))
        data = {
            "Images": binaryData,
            "Title": info["title"],
            "Location": info["location"],
            "Description": info["desc"],
            "StartPrice": info["StartPrice"],
            "EndPrice": info["EndPrice"],
        }
        self.setID(Database().Insert("Post", data))
        self.setDescription(info["desc"])
        self.setImages(imagesPath)
        self.setLocation(info["location"])
        self.setTitle(info["title"])
        self.setStartPrice(info["StartPrice"])
        self.setEndPrice(info["EndPrice"])

    def getPostByID(self, ID):
        result = Database().SelectByID("Post", ID)
        if result:
            self.setDescription(result["desc"])
            self.setImages(result["images"])
            self.setLocation(result["location"])
            self.setTitle(result["title"])
            self.setStartPrice(result["StartPrice"])
            self.setEndPrice(result["EndPrice"])

    def editData(self, query, ID):
        Database().UpdateOne("User", ID, query)

    def addToImages(self, ID, imagePath):
        images = self.getImages()
        images.append(imagePath)
        self.setImages(images)
        Database().AddToRecord("Post",)
