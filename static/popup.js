// Get the DOM elements for the image carousel
const wrapper = document.querySelector(".wrapper"),
  carousel = document.querySelector(".carousel"),
  images = document.querySelectorAll("img"),
  buttons = document.querySelectorAll(".button");

let imageIndex = 1,
  intervalId;

// Define function to start automatic image slider
const autoSlide = () => {
  // Start the slideshow by calling slideImage() every 2 seconds
  intervalId = setInterval(() => slideImage(++imageIndex), 2000);
};
// Call autoSlide function on page load
autoSlide();

// A function that updates the carousel display to show the specified image
const slideImage = () => {
  // Calculate the updated image index
  imageIndex = imageIndex === images.length ? 0 : imageIndex < 0 ? images.length - 1 : imageIndex;
  // Update the carousel display to show the specified image
  carousel.style.transform = `translate(-${imageIndex * 100}%)`;
};

// A function that updates the carousel display to show the next or previous image
const updateClick = (e) => {
  // Stop the automatic slideshow
  clearInterval(intervalId);
  // Calculate the updated image index based on the button clicked
  imageIndex += e.target.id === "next" ? 1 : -1;
  slideImage(imageIndex);
  // Restart the automatic slideshow
  autoSlide();
};

// Add event listeners to the navigation buttons
buttons.forEach((button) => button.addEventListener("click", updateClick));

// Add mouseover event listener to wrapper element to stop auto sliding
wrapper.addEventListener("mouseover", () => clearInterval(intervalId));
// Add mouseleave event listener to wrapper element to start auto sliding again
wrapper.addEventListener("mouseleave", autoSlide);


////liked post
const favoriteButtons = document.querySelectorAll('.favorite-btn');

favoriteButtons.forEach(button => {
  button.addEventListener('click', function () {
    const imageId = this.getAttribute('data-id');

    // Perform action with the imageId (e.g., store it as a favorite)
    console.log(`Image ${imageId} is liked.`);
    // Toggle the 'liked' class to change the heart color


    // Send a request to the backend to store or remove the liked image
    fetch('/like', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ imageId }) // Send the imageId to the server
    })
      .then(response => {
        if (response.ok) {
          console.log('Like status updated successfully.');
        } else {
          console.error('Failed to update like status.');
        }
      })
      .catch(error => console.error('Error:', error));
  });
});



const favoriteBtn = document.querySelector('.favorite-btn');

favoriteBtn.addEventListener('click', async () => {
  const postId = favoriteBtn.getAttribute('data-id');
  this.classList.toggle('liked');
  try {
    const response = await fetch(`/add_to_favorites/${postId}`, {
      method: 'POST',
      // Add any necessary headers or body data
    });
    if (response.ok) {
      // Handle success, maybe update UI to indicate the post is now a favorite
      console.log('Post added to favorites!');
    } else {
      // Handle error case
      console.error('Failed to add post to favorites');
    }
  } catch (error) {
    console.error('Error occurred:', error);
  }
});