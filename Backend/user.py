from db import Database
import hashlib
from bson import Binary


class User:
    def __init__(self):
        _id = None
        _userName = None
        _password = None
        _post = None
        _favorite = None
        _numberOfFollowers = None
        _numberOfFollowing = None
        _bio = None
        _profilePicture = None

    def setProfilePicture(self, ProfilePicture):
        self._profilePicture = ProfilePicture

    def setUserName(self, UserName):
        self._userName = UserName

    def setPassword(self, Password):
        self._password = Password

    def setFavorite(self, Favorite):
        self._favorite = Favorite

    def setPost(self, Post):
        self._post = Post

    def setBio(self, Bio):
        self._bio = Bio

    def setNumberOfFollowers(self, NumberOfFollowers):
        self._numberOfFollowers = NumberOfFollowers

    def setNumberOfFollowing(self, NumberOfFollowing):
        self._numberOfFollowing = NumberOfFollowing

    def setID(self, ID):
        self._id = ID

    def getProfilePicture(self):
        return self._profilePicture

    def getUserName(self):
        return self._userName

    def getPassword(self):
        return self._password

    def getFavorite(self):
        return self._favorite

    def getPost(self):
        return self._post

    def getBio(self):
        return self._bio

    def getNumberOfFollowers(self):
        return self._numberOfFollowers

    def getNumberOfFollowing(self):
        return self._numberOfFollowing

    def getID(self):
        return self._id

    def Login(self, userName, password):
        data = {"userName": userName}
        result = Database().SelectCollection("User", data)
        if result:
            hashedPassword = hashlib.sha256(password.encode()).hexdigest()
            if result[0]["password"] == hashedPassword:
                self.setID(result[0]["_id"])
                self.setUserName(result[0]["userName"])
                self.setPassword(result[0]["password"])
                self.setProfilePicture(result[0]["profilePicture"])
                if "post" in result[0]:
                    self.setPost(result[0]["post"])
                if "favorite" in result[0]:
                    self.setFavorite(result[0]["favorite"])
                self.setNumberOfFollowers(result[0]["numberOfFollowers"])
                self.setNumberOfFollowing(result[0]["numberOfFollowing"])
                if "bio" in result[0]:
                    self.setBio(result[0]["bio"])
                return True
            else:
                return "Wrong Password"
        else:
            return "User Not Found"

    def SignUp(self, userName, password):
        hashedPassword = hashlib.sha256(password.encode()).hexdigest()
        data = {"userName": userName, "password": hashedPassword}
        _id = Database().Insert("User", data)
        self.setInformation(_id)
        return _id

    def setInformation(self, ID):
        with open("static/images/defaultProfilePicture.jpg", "rb") as file:
            image_data = file.read()
        binaryData = Binary(image_data)
        query = {
            "$set": {
                "numberOfFollowers": 0,
                "numberOfFollowing": 0,
                "profilePicture": binaryData,
            }
        }
        Database().UpdateOne("User", ID, query)

    def addBio(self, ID, bio):
        query = {"bio": bio}
        Database().UpdateOne("User", ID, query)

    def putProfilePicture(self, ID, imagePath):
        with open(imagePath, "rb") as file:
            imageData = file.read()
        binaryData = Binary(imageData)
        query = {"$set": {"profilePicture": binaryData}}
        self._profilePicture = binaryData
        Database().UpdateOne("User", ID, query)

    def getUserByID(self, ID):
        result = Database().SelectByID("User", ID)
        if result:
            if "bio" in result:
                self.setBio(result["bio"])
            if "post" in result:
                self.setPost(result["post"])
            if "favorite" in result:
                self.setFavorite(result["favorite"])
            self.setID(result["_id"])
            self.setUserName(result["userName"])
            self.setPassword(result["password"])
            self.setProfilePicture(result["profilePicture"])
            self.setNumberOfFollowers(result["numberOfFollowers"])
            self.setNumberOfFollowing(result["numberOfFollowing"])
