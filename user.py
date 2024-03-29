from db import Database
import hashlib
from bson import ObjectId


class User:
    def __init__(self):
        self._id = None
        self._userName = None
        self._password = None
        self._favorite = []
        self._posts = []
        self._profilePicture = None

    def setProfilePicture(self, ProfilePicture):
        self._profilePicture = ProfilePicture

    def setUserName(self, UserName):
        self._userName = UserName

    def setPassword(self, Password):
        self._password = Password

    def setFavorite(self, Favorite):
        self._favorite = Favorite

    def setID(self, ID):
        self._id = str(ID)

    def setPosts(self, posts):
        self._posts = posts

    def getPosts(self):
        return self._posts

    def getProfilePicture(self):
        return str(self._profilePicture)

    def getUserName(self):
        return self._userName

    def getPassword(self):
        return self._password

    def getFavorite(self):
        return self._favorite

    def getID(self):
        return self._id

    def Login(self, userName, password):
        data = {"Username": userName}
        result = Database().SelectCollection("User", data)
        if result:
            hashedPassword = hashlib.sha256(password.encode()).hexdigest()
            if result[0]["Password"] == hashedPassword:
                self.setID(result[0]["_id"])
                self.setUserName(result[0]["Username"])
                self.setPassword(result[0]["Password"])
                self.setProfilePicture(result[0]["ProfilePicture"])
                if "Posts" in result[0]:
                    self.setPosts(result[0]["Posts"])
                if "Favorite" in result[0]:
                    self.setFavorite(result[0]["Favorite"])
                return True
            else:
                return "Wrong Password"
        else:
            return "User Not Found"

    def SignUp(self, userName, password):
        hashedPassword = hashlib.sha256(password.encode()).hexdigest()
        data = {"Username": userName, "Password": hashedPassword}
        _id = Database().Insert("User", data)
        query = {
            "$set": {
                "ProfilePicture": "defaultProfilePicture.jpg",
            }
        }
        self.editData(query, _id)
        return _id

    def editData(self, query, ID):
        Database().UpdateOne("User", ID, query)

    def getUserByID(self, ID):
        result = Database().SelectByID("User", ID)
        if result:
            if "Favorite" in result:
                self.setFavorite(result["Favorite"])
            if "Posts" in result:
                self.setPosts(result["Posts"])
            self.setID(result["_id"])
            self.setUserName(result["Username"])
            self.setPassword(result["Password"])
            self.setProfilePicture(result["ProfilePicture"])

    def deleteAccount(self):
        Database().DeleteID("User", self.getID())

    def removeFromFavorite(self, postID):
        posts = self.getFavorite()
        posts.remove(postID)
        self.setFavorite(posts)
        data = {"Favorite": postID}
        Database().RemoveFromRecord("User", self.getID(), data)

    def addToFavorite(self, postID):
        posts = self.getFavorite()
        posts.append(postID)
        self.setFavorite(posts)
        data = {"Favorite": postID}
        Database().AddToRecord("User", self.getID(), data)

    def getFieldFromUser(self, param, col):
        data = Database().SelectRecordCollection("User", param, col)
        return data

    def addPost(self, postID):
        post = self.getPosts()
        post.append(postID)
        self.setPosts(post)
        data = {"Posts": postID}
        Database().AddToRecord("User", self.getID(), data)
