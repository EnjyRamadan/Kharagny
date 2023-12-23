# from user import User

# user = User()
# # user.Login("mazennashraff1", "_Mazen722003")
from io import BytesIO
from PIL import Image


image = Image.open(BytesIO(binary_data))
image.show()