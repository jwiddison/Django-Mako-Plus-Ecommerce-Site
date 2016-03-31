$(function() {

  // Hides the quantity field on the form if the product is an individual product.
  if($('#Quantity_Form_Button').attr('data-ptype') === 'Individual Product')
  {
    $('#id_quantity').closest("table").hide();
    $('#id_quantity').hide();
  }

  $('.detail > a').click(function(event) {
    event.preventDefault();
    $.loadmodal({
      // url: detail_ul,
      url: '/catalog/detail.carousel/' + $(this).attr('data-pid'),
      title: 'All Images For ' + $(this).attr('data-pname') + ':',
      id: 'product_image_carousel',
      width: '600px',
    }); // LoadModal
  }); // click

}); // ready
