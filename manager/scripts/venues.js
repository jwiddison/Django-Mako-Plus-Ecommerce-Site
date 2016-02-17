$(function() {
  $('.delete_venue_button').click(function( event ) {
    // Stop href from executing
    event.preventDefault();

    // Store url in variable
    var url = $(this).attr('href');

    // Set href of button in modal
    $('#confirm_delete_venue_button').attr('href', url);

    // Show the modal
    $('#delete_venue_modal').modal('show');
  });
}); //Function to user delete modal
