function sendData() {
  const imageFile = document.getElementById('imageFile').files[0];
  const Title = document.getElementById('Title').value;
  const Location = document.getElementById('Location').value;
  const Description = document.getElementById('Description').value;
  
  fetch("http://localhost:5000/call_function", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      imageFile: imageFile,
      Title: Title,
      Location: Location,
      Description: Description,

    }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Log the result in the console
      console.log("Result:", data.result);
    })
    .catch((error) => console.error("Error:", error));
}
