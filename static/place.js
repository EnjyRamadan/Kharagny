
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

// function sendData() {
//   const imageFiles = document.getElementById('imageFiles').files; // Updated to get all files
//   const Title = document.getElementById('Title').value;
//   const Location = document.getElementById('Location').value;
//   const Description = document.getElementById('Description').value;
//   const range1 = document.getElementById('range1').value;
//   const range2 = document.getElementById('range2').value;
//   const category = document.getElementById('category').value;

//   const formData = new FormData();
//   for (let i = 0; i < imageFiles.length; i++) {
//     formData.append('imageFiles', imageFiles[i]);
//   }
//   formData.append('Title', Title);
//   formData.append('Location', Location);
//   formData.append('Description', Description);
//   formData.append('range1', range1);
//   formData.append('range2', range2);
//   formData.append('category', category);
  

//   fetch("http://127.0.0.1:5000/call_function", {
//     method: "POST",
//     // body: formData,  // Update to formData
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       // console.log("Result:", data.Title, data.Description, data.Location, data.imageFile, data.range1, data.range2, data.strategy);
//     })
//     .catch((error) => console.error("Error:", error));
// }
