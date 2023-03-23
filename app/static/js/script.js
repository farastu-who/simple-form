// Wait for the document to finish loading before adding event listeners
document.addEventListener('DOMContentLoaded', function() {
  
    // Find the submit button in the input form
    var submitButton = document.querySelector('form input[type="submit"]');
    
    // Add an event listener to the submit button
    submitButton.addEventListener('click', function(event) {
      
      // Show a confirmation dialog before submitting the form
      var confirmed = confirm('Are you sure you want to submit this input?');
      
      // If the user clicks "Cancel", prevent the form from being submitted
      if (!confirmed) {
        event.preventDefault();
      }
    });
    
    // Format timestamps to a more readable format
    var timestamps = document.querySelectorAll('.timestamp');
    for (var i = 0; i < timestamps.length; i++) {
      var timestamp = timestamps[i];
      timestamp.textContent = formatTime(timestamp.textContent);
    }
    
    // Format time using Moment.js library
    function formatTime(timestamp) {
      var momentTime = moment(timestamp);
      return momentTime.format('MMMM Do YYYY, h:mm:ss a');
    }
  });
  