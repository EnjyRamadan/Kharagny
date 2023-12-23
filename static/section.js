document.addEventListener("DOMContentLoaded", function () {
  const scrollRight = document.getElementById("scrollRightAdventures");
  const scrollLeft = document.getElementById("scrollLeftAdventures");
  const productListContainer = document.querySelector(
    ".product-list-container-Adventures"
  );

  console.log("Initial Scroll Left:", productListContainer.scrollLeft);
  console.log("Initial Scroll Right:", productListContainer.scrollRight);

  scrollRight.addEventListener("click", function () {
    console.log("Clicked!");
    productListContainer.scrollBy({
      top: 0,
      left: 620,
      behavior: "smooth",
    });
    console.log("Scroll Left After:", productListContainer.scrollLeft);
  });

  scrollLeft.addEventListener("click", function () {
    console.log("Clicked!");
    productListContainer.scrollBy({
      top: 0,
      left: -620,
      behavior: "smooth",
    });
    console.log("Scroll Left After:", productListContainer.scrollLeft);
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const scrollRight = document.getElementById("scrollRightDate");
  const scrollLeft = document.getElementById("scrollLeftDate");
  const productListContainer = document.querySelector(
    ".product-list-container-Date"
  );

  console.log("Initial Scroll Left:", productListContainer.scrollLeft);
  console.log("Initial Scroll Right:", productListContainer.scrollRight);

  scrollRight.addEventListener("click", function () {
    console.log("Clicked!");
    productListContainer.scrollBy({
      top: 0,
      left: 620,
      behavior: "smooth",
    });
    console.log("Scroll Left After:", productListContainer.scrollLeft);
  });

  scrollLeft.addEventListener("click", function () {
    console.log("Clicked!");
    productListContainer.scrollBy({
      top: 0,
      left: -620,
      behavior: "smooth",
    });
    console.log("Scroll Left After:", productListContainer.scrollLeft);
  });
});
