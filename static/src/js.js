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

function showLoader() {
  document.getElementById('loader').style.display = 'flex';
}

function hideLoader() {
  document.getElementById('loader').style.display = 'none';
}

// Example AJAX request using Fetch API
function fetchData() {
  showLoader();
  fetch('your-api-endpoint')
      .then(response => response.json())
      .then(data => {
          // Process your data here
      })
      .catch(error => {
          // Handle the error
      })
      .finally(() => {
          hideLoader();
      });
}




document.addEventListener('alpine:init', () => {
  Alpine.data('skillDisplay', () => ({
      skills: [{
              'title': 'HTML',
              'percent': '95',
          },
          {
              'title': 'CSS',
              'percent': '70',
          },
          {
              'title': 'Tailwind CSS',
              'percent': '70',
          },
          {
              'title': 'Python',
              'percent': '65',
          },
          {
              'title': 'SQL',
              'percent': '60',
          }, {
              'title': 'Javascript',
              'percent': '65',
          }
      ],
      currentSkill: {
          'title': 'HTML',
          'percent': '95',
      }
  }));
});