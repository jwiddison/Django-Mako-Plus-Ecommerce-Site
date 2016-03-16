<%! import json %>

$(function() {

  var filenames = ${ json.dumps(images) };
  var index = 0;

  $('.next_button').click(function() {
    index += 1;
    $('.product_image').attr('src', '/catalog/media/pics/' + filename[index]);
  });

  $('.previous_button').click(function() {
    index -= 1;
    $('.product_image').attr('src', '/catalog/media/pics/' + filename[index]);
  });


  // $('.product_image').first().removeClass('hide');
  // $('.next_button').click(function() {
  //   var current = $('.product_image:not(.hide)');
  //   var next = current.next('.product_image');
  //   current.addClass('hide');
  //   next.removeClass('hide');
  // });

});//ready
