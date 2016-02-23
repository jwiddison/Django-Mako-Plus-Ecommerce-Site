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
