$(function() {
  $('.delete_product_button').click(function( event ) {
    event.preventDefault();
    var url = $(this).attr('href');
    $('#confirm_delete_product_button').attr('href', url);
    $('#delete_product_modal').modal('show');
  });
});

$('.glyphicon').click(function( event ) {
    event.preventDefault();
    var href = $(this).attr("href");//getting id
      $(this).siblings('.quantity').load(href);
 });
