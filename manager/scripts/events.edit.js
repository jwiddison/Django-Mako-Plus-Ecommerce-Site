// DELETE MODAL //
$(function() {
  $('.delete_area_button').click(function( event ) {
    event.preventDefault();
    var url = $(this).attr('href');
    $('#confirm_delete_area_button').attr('href', url);
    $('#delete_area_modal').modal('show');
  });
});

// EDIT AREA //
// $(function() {
//   $('.edit_area_button').click(function() {
//     $.loadmodal({
//       url: '/manager/areas.edit/',
//       id: 'edit_area_modal',
//       title: 'Edit Area Info:',
//     });
//   });
// });
//
// // $(function() {
// //   $('.edit_area_button').click(function( event ) {
// //     event.preventDefault();
// //     var url = $(this).attr('href');
// //     $('#confirm_edit_area_button').attr('href', url);
// //     $('#edit_area_modal').modal('show');
// //   });
// // });
//
// $(function() {
//   $('#edit_area_form').ajaxForm({
//     // Replace form in its immediate parent.
//     target: '#jquery-loadmodal-js-body',
//   }); //ajaxform
// });


// CREATE A NEW AREA //
// $(function() {
//   $('#new_area_button').click(function(event) {
//     event.preventDefault();
//     $.loadmodal({
//       url: '/manager/areas.create/',
//       id: 'create_area_modal',
//       title: 'Create A New Area at this Event:',
//     });
//   });
// });
//
// $(function() {
//   $('#create_area_form').ajaxForm({
//     // Replace form in its immediate parent.
//     target: '#jquery-loadmodal-js-body',
//   }); //ajaxform
// });
