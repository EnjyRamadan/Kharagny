from user import User
from io import BytesIO
from PIL import Image

user = User()
image = Image.open(BytesIO(user._profilePicture))
image.show()
