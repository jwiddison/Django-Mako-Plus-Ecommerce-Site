$(function(){
  $('#modal_trigger_image').click(function() {
    $(this).preventDefault();
    $.loadmodal({
      url: '/catalog/detail.carousel/${ p.id }',
      // id: 'product_images_modal',
    }); // LoadModal
  });
});//ready
