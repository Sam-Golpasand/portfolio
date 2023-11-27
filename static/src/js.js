// Set a timeout of 5000 milliseconds (5 seconds)
setTimeout(function() {
  // Select the flash message container
  var flashMessage = document.getElementById('flash-message');
  // Check if it exists
  if (flashMessage) {
    // Fade out the flash message
    flashMessage.style.opacity = '0';
    // Optional: remove the flash message element after the fade-out transition
    setTimeout(function() {
      flashMessage.style.display = 'none';
    }, 600); // Adjust timing to match your CSS transition
  }
}, 5000); // Time in milliseconds before the flash message disappears


// JavaScript to handle hover state color change for links
document.querySelectorAll('nav a').forEach(link => {
  link.onmouseover = () => link.style.backgroundColor = '#005B41';
  link.onmouseout = () => link.style.backgroundColor = '';
});
