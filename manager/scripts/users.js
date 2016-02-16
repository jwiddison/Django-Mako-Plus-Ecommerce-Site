$(function() {
  $('delete_button').click(function() {
    // Store url in variable
    var url = $('delete_button').attr('href')
    // Set href of button in modal
    $('#confirm_delete_button').attr('href', url)
    // Show the modal
    $('#delete_modal').modal('show')
  });
});

//Functionally:
// 1. Use jQuery to grab value of href attribute
// 2. Put it in the empty href in the modal
// 3.
// 4.
