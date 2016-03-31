$(function() {
  $('#loginbutton').click(function() {
    $.loadmodal({
      url: '/account/login/',
      id: 'loginmodal',
      title: 'Login to ColonialHeritage.org',
      width: '500px',
    }); // LoadModal
  }); // Click

  var windowHeight = $(window).height();
  $('.parallax-window').css('min-height', windowHeight);

}); // Ready
