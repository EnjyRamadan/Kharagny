from db import Database
import hashlib
from bson import Binary

class User:
    _id = None
    _userName = None
    _password = None
    _post = None
    _favorite = None
    _numberOfFollowers = None
    _numberOfFollowing = None
    _bio = None
    _profilePicture = None

    def Login(self, userName, password):
        data = {"userName": userName}
        result = Database().SelectCollection("User", data)
        if result:
            print(result)
            hashedPassword = hashlib.sha256(password.encode()).hexdigest()
            if result[0]["password"] == hashedPassword:
                self._id = result[0]["_id"]
                self._userName = result[0]["userName"]
                self._password = result[0]["password"]
                if "post" in result[0]:
                    self._post = result[0]["post"]
                if "favorite" in result[0]:
                    self._favorite = result[0]["favorite"]
                self._numberOfFollowers = result[0]["numberOfFollowers"]
                self._numberOfFollowing = result[0]["numberOfFollowing"]
                if "bio" in result[0]:
                    self._bio = result[0]["bio"]
                if "profilePicture" in result[0]:
                    self._profilePicture = result[0]["profilePicture"]
                return True
            else:
                return "Wrong Password"
        else:
            return "User Not Found"

    def SignUp(self, userName, password):
        hashedPassword = hashlib.sha256(password.encode()).hexdigest()
        data = {"userName": userName, "password": hashedPassword}
        _id = Database().Insert("User", data)
        return _id

    def setInformation(self, info):
        _id = info["id"]
        with open("static/images/defaultProfilePicture.jpg", "rb") as file:
            image_data = file.read()
        binary_data = Binary(image_data)
        query = {
            "$set": {
                "numberOfFollowers": 0,
                "numberOfFollowing": 0,
                "profilePicture": binary_data
            }
        }
        Database().UpdateOne("User", _id, query)
