const wrapper = document.querySelector(".wrapper");
const carousel = document.querySelector(".carousel");
const images = document.querySelectorAll(".img");
let imageIndex = 0;
let intervalId;
const autoSlide = () => {
  if (images.length > 1) {
    intervalId = setInterval(() => slideImage(++imageIndex), 2000);
  }
};
const slideImage = (index) => {
  const slideDistance = 80;
  imageIndex = index >= images.length ? 0 : index < 0 ? images.length - 1 : index;
  carousel.style.transform = `translate(-${imageIndex * slideDistance}%)`;
};
const updateClick = (e) => {
  clearInterval(intervalId);
  imageIndex += e.target.id === "next" ? 1 : -1;
  slideImage(imageIndex);
  autoSlide();
};
wrapper.addEventListener("mouseover", () => clearInterval(intervalId));
wrapper.addEventListener("mouseleave", autoSlide);
const likeButton = document.querySelector('.favorite-btn');
likeButton.addEventListener('click', function () {
  const imageId = this.getAttribute('data-id');
  console.log(`Image ${imageId} is liked.`);
});
autoSlide();
document.addEventListener('DOMContentLoaded', function () {
  const heartIcon = document.getElementById('heart');
  let isFavorite = heartIcon.dataset.isFavorite === 'true';
  // Accessing the custom attribute
  // Function to update the heart icon based on the current state
  const updateHeartIcon = () => {
    if (isFavorite) {
      heartIcon.classList.add('active'); // Add a class for the red heart icon
    } else {
      heartIcon.classList.remove('active'); // Remove the class for the white heart icon
    }
  };
  // Update the heart icon on page load
  updateHeartIcon();
  heartIcon.addEventListener('click', function () {
    const postId = heartIcon.dataset.id;
    console.log(postId)
    fetch(`/like/${postId}`, {
      method: 'POST',
    })
      .then(response => {
        if (response.ok) {
          isFavorite = !isFavorite; // Toggle the favorite state on successful response
          updateHeartIcon(); // Update the heart icon appearance
          return response.json(); // Parse the JSON response
        } else {
          throw new Error('Network response was not ok.');
        }
      })
      .then(data => {
        console.log('Success:', data.message); // Handle successful response
        // You can update UI or show a success message here
      })
      .catch(error => {
        console.error('Error occurred while sending like:', error);
        // You can show an error message or perform error handling here
      });
  });
});
