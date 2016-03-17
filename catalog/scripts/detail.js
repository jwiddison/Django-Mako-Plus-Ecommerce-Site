$(function() {

  $('.detail > a').click(function(event) {
    event.preventDefault();

    // var detail_url = $(this).attr('href');
    //console.log(detail_url); // Just to check and make sure we're pulling the right URL

    $.loadmodal({
      // url: detail_ul,
      url: '/catalog/detail.carousel/' + $(this).attr('data-pid'),
      title: 'All Images For ' + $(this).attr('data-pname') + ':',
      id: 'product_image_carousel',
      width: '600px',
    }); // LoadModal
  }); // click

}); // ready
