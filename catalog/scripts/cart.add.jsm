$(function(){
  $('.add_form > form').ajaxForm({
  // $('#add_form').ajaxForm({
    target: $('#add_form_placeholder'),
  });
  $('#cartbutton > .cart_quantity').text('${request.shopping_cart.get_item_count()}');
});
