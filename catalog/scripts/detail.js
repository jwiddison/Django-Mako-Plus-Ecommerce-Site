$(function() {

  $('#load_carousel').click(function(event) {
    event.preventDefault();

    var detail_url = $(this).attr('href');
    //console.log(detail_url); // Just to check and make sure we're pulling the right URL

    var product_name = $(this).attr('data-pname');

    $.loadmodal({
      url: detail_url,
      title: 'All Images For ' + product_name + ':',
      id: 'product_image_carousel',
      width: '600px',
    }); // LoadModal
  }); // click

}); // ready
