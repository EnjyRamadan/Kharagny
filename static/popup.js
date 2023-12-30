
    const wrapper = document.querySelector(".wrapper");
    const carousel = document.querySelector(".carousel");
    const images = document.querySelectorAll(".img");
    let imageIndex = 0;
    let intervalId;

    const autoSlide = () => {
      // Check if there is more than one image
      if (images.length > 1) {
          intervalId = setInterval(() => slideImage(++imageIndex), 2000);
      }
  };
  
    const slideImage = (index) => {
        imageIndex = index >= images.length ? 0 : index < 0 ? images.length - 1 : index;
        carousel.style.transform = `translate(-${imageIndex * 100}%)`;
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
        // Add your logic to handle the like button click
        const imageId = this.getAttribute('data-id');
        console.log(`Image ${imageId} is liked.`);
        // Perform additional actions as needed
    });

    // Initialize the image slider
    autoSlide();



    const heartButton = document.getElementById('heart');

  // Add a click event listener to the heart button
  heartButton.addEventListener('click', function () {
    // Toggle the 'red-heart' class to change the color
    this.classList.toggle('red-heart');
    const imageId = this.getAttribute('data-id');
    console.log(`Image ${imageId} is liked.`);

    // Perform additional actions as needed
  });