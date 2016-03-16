$(function() {
  $('#load_carousel').click(function(event) {
    event.preventDefault();
    var detail_url = $(this).attr('href');
    var pname = $(this).attr('data-pname');
    console.log(detail_url);
    // // Load url into modal
    // $.loadmodal(String(detail_url));
    $.loadmodal({
      url: detail_url,
      title: 'All images for ' + pname + ':',
      id: 'product_image_carousel',
      width: '650px',
    }); // LoadModal
  }); // click
}); // ready
