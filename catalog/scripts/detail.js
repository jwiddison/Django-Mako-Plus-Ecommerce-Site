$(function(){
  $('#modal_trigger_image').click(function() {
    $.loadmodal({
      url: '/catalog/detail.carousel/',
      // id: 'product_images_modal',
    }); // LoadModal
  });
});//ready
