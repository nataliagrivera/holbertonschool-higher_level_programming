// 2-script.js

// Use document.querySelector to select the element with id "red_header"
var redHeaderElement = document.querySelector("#red_header");

// Add a click event listener to the selected element
redHeaderElement.addEventListener("click", function() {
  // Use document.querySelector to select the header element
  var headerElement = document.querySelector("header");

  // Add the class "red" to the header element
  headerElement.classList.add("red");
});
