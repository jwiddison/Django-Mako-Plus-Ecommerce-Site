$(function() {
  $('.delete_area_button').click(function( event ) {
    // Stop href from executing
    event.preventDefault();

    // Store url in variable
    var url = $(this).attr('href');

    // Set href of button in modal
    $('#confirm_delete_area_button').attr('href', url);

    // Show the modal
    $('#delete_area_modal').modal('show');
  });
}); //Function to user delete modal

$(function() {
  $('#areaform').ajaxForm({
    // Replace form in its immediate parent.
    target: '#jquery-loadmodal-js-body',
  }); //ajaxform
}); //Ready

$(function() {
  $('.edit_area_button').click(function() {
    $.loadmodal({
      url: '/manager/areas.edit/',
      id: 'edit_area_modal',
      title: 'Edit area:',
      width: '500px',
    }); // LoadModal
  }); // Click
}); // Ready
