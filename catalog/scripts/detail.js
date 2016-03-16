$(function(){
  $('#modal_trigger_image').click(function(event) {
    event.preventDefault();
    var detail_url = $(this).attr('href');
    console.log(detail_url);
    // Load url into modal
    $.loadmodal('/catalog/detail.carousel/');

    // $.loadmodal({
    //   url: detail_url,
    //   id: 'product_images_modal',
    // }); // LoadModal
  }); // click
}); // ready
