$(function() {

  var index = 0;

  var filenames = [
    %for pi in p_images:
      "${ pi.filename }",
    %endfor
  ]

  $('#previous_button').click(function() {
    index -= 1;
    if (index < 0){
      index = 3;
    }
    $('#pimage').attr('src', '${ STATIC_URL }/catalog/media/pics/' + filenames[index]);
  }); // Click

  $('#next_button').click(function() {
    index += 1;
    if (index > 3){
      index = 0;
    }
    $('#pimage').attr('src', '${ STATIC_URL }/catalog/media/pics/' + filenames[index]);
  }); // Click

}); // Ready
