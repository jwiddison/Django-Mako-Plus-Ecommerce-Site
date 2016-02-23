$(function() { //Shows delete modal and passes ID
  $('.delete_area_button').click(function( event ) {
    event.preventDefault();
    var url = $(this).attr('href');
    $('#confirm_delete_area_button').attr('href', url);
    $('#delete_area_modal').modal('show');
  });
});



$(function() {
  $('.edit_area_button').click(function( event ) {
    event.preventDefault();
    $.loadmodal({
      url: '/manager/areas.edit/',
      id: 'edit_area_modal',
      title: 'Edit Area:',
      width: '500px',
    });
  });
});

$(function() {
  $('#new_area_button').click(function(event) {
    event.preventDefault();
    $.loadmodal({
      url: '/manager/areas.create/',
      id: 'create_area_modal',
      title: 'Create A New Area:',
      width: '500px',
    });
  });
});

$(function() {
  $('#create_area_form').ajaxForm({
    // Replace form in its immediate parent.
    target: '#jquery-loadmodal-js-body',
  }); //ajaxform
});
