$(document).ready(function() {
    // Attach a click event handler to the upload button
    $('#uploadButton').on('click', function() {
      // Get the file input element
      const fileInput = $('#fileInput')[0];
  
      // Create a new FormData object
      const formData = new FormData();
  
      // Add the file to the FormData object
      formData.append('file', fileInput.files[0]);
  
      // Use jQuery to send an AJAX request
      $.ajax({
        url: 'http://localhost:8000/uploadfile',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
          // Display the server's response in a div element
          $('#responseDiv').text(response.result);
        },
        error: function(xhr, status, error) {
          console.error('Error uploading file:', error);
        }
      });
    });
});