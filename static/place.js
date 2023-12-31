
function previewImages(event) {
  const files = event.target.files;

  const imagesContainer = document.getElementById('uploadedImagesContainer');
  imagesContainer.innerHTML = ''; // Clear previous images

  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    const reader = new FileReader();

    reader.onload = function (e) {
      const img = document.createElement('img');
      img.src = e.target.result;
      img.className = 'uploaded-image';
      imagesContainer.appendChild(img);
    };

    reader.readAsDataURL(file);
  }
}