<%! import json %>

$(function() {

  var filenames = ${ json.dumps(images) };
  var index = 0;

  $('.next_button').click(function() {
    index += 1;
    if index >= 3{
      index = 0;
    }
    $('.product_image').attr('src', '${ STATIC_URL }/catalog/media/pics/' + filename[index]);
  });

  $('.previous_button').click(function() {
    index -= 1;
    if index < 0{
      index = 3;
    }
    $('.product_image').attr('src', '${ STATIC_URL }/catalog/media/pics/' + filename[index]);
  });


  // $('.product_image').first().removeClass('hide');
  // $('.next_button').click(function() {
  //   var current = $('.product_image:not(.hide)');
  //   var next = current.next('.product_image');
  //   current.addClass('hide');
  //   next.removeClass('hide');
  // });

});//ready
