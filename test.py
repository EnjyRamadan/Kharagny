from post import Post
imagesPath = ["download.jpg", "landscape.png"]  # Replace these with actual image file names
info = {
      "Images": imagesPath,
     "Title": "Cosmo City",
      "Category": "Arcade",
      "Location": "Zayed",
      "Description": "includes laser tags",
      "StartPrice": 200,
      "EndPrice": 600,
}

# Call the createPost method
post = Post()  # Assuming Post is the class where createPost is defined
post.createPost(imagesPath, info)
