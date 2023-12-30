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

const heartButton = document.getElementById('heart');


heartButton.addEventListener('click', function () {
  
  this.classList.toggle('red-heart');
  const imageId = this.getAttribute('data-id');
  console.log(`Image ${imageId} is liked.`);

 
});
