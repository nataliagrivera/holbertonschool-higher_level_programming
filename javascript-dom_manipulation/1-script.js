// 1-script.js

// Use document.querySelector to select the element with id "red_header"
var redHeaderElement = document.querySelector("#red_header");

// Add a click event listener to the selected element
redHeaderElement.addEventListener("click", function() {
  // Use document.querySelector to select the header element
  var headerElement = document.querySelector("header");

  // Update the text color of the header element to red (#FF0000)
  headerElement.style.color = "#FF0000";
});
