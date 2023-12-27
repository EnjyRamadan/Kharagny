from db import Database
import hashlib
from bson import Binary


class User:
    def __init__(self):
        self._id = None
        self._userName = None
        self._password = None
        self._favorite = []
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
        self._id = ID

    def getProfilePicture(self):
        return self._profilePicture

    def getUserName(self):
        return self._userName

    def getPassword(self):
        return self._password

    def getFavorite(self):
        return self._favorite

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
                if "favorite" in result[0]:
                    self.setFavorite(result[0]["favorite"])
                return True
            else:
                return "Wrong Password"
        else:
            return "User Not Found"

    def SignUp(self, userName, password):
        hashedPassword = hashlib.sha256(password.encode()).hexdigest()
        data = {"userName": userName, "password": hashedPassword}
        _id = Database().Insert("User", data)
        with open("static/images/defaultProfilePicture.jpg", "rb") as file:
            image_data = file.read()
        binaryData = Binary(image_data)
        query = {
            "$set": {
                "profilePicture": binaryData,
            }
        }
        self.editData(query, _id)
        return _id

    def editData(self, query, ID):
        Database().UpdateOne("User", ID, query)

    def getUserByID(self, ID):
        result = Database().SelectByID("User", ID)
        if result:
            if "favorite" in result:
                self.setFavorite(result["favorite"])
            self.setID(result["_id"])
            self.setUserName(result["userName"])
            self.setPassword(result["password"])
            self.setProfilePicture(result["profilePicture"])
