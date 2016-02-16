$(function() {
  $('.delete_button').click(function( event ) {
    // Stop href from executing
    event.preventDefault();

    // Store url in variable
    var url = $(this).attr('href');

    console.log(url);

    // Set href of button in modal
    $('#confirm_delete_button').attr('href', url);

    // Show the modal
    $('#delete_modal').modal('show');
  });
});
