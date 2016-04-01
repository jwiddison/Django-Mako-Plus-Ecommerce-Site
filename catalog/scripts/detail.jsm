$(function() {
  //Load modal for image carousel
  $('.detail > a').click(function(event) {
    event.preventDefault();
    $.loadmodal({
      url: '/catalog/detail.carousel/' + $(this).attr('data-pid'),
      title: 'All Images For ' + $(this).attr('data-pname') + ':',
      id: 'product_image_carousel',
      width: '600px',
    }); // LoadModal
  }); // click

  //Load the add form using AJAX
  $('#add_form_placeholder').load("/catalog/cart.add/${p.id}");
}); // ready
