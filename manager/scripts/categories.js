$(function() {
  $('.delete_category_button').click(function( event ) {
    // Stop href from executing
    event.preventDefault();

    // Store url in variable
    var url = $(this).attr('href');

    // Set href of button in modal
    $('#confirm_delete_category_button').attr('href', url);

    // Show the modal
    $('#delete_category_modal').modal('show');
  });
}); //Function to user delete modal
