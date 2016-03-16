// <%! import json %>
$(function() {

  // var filenames = ${ json.dumps(images) };

  // var filenames = [
  //   %for pi in images:
  //     '${ pi.filename }'
  //   %endfor
  // ]

  var index = 0;

  console.log('test1');


  $('#next_button').click(function() {
    index += 1;
    // if index >= 3{
    //   index = 0;
    // }
    console.log('test2');
    $('#product_image').attr('src', '${ STATIC_URL }/catalog/media/pics/' + filenames[index]);
  });

  $('#previous_button').click(function() {
    index -= 1;
    // if index < 0{
    //   index = 3;
    // }
    $('#product_image').attr('src', '${ STATIC_URL }/catalog/media/pics/' + filenames[index]);
  });


  // $('.product_image').first().removeClass('hide');
  // $('.next_button').click(function() {
  //   var current = $('.product_image:not(.hide)');
  //   var next = current.next('.product_image');
  //   current.addClass('hide');
  //   next.removeClass('hide');
  // });

});
