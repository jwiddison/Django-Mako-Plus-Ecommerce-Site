$(function() {
  $('#loginbutton').click(function() {
    $.loadmodal({
      url: '/account/login/',
      id: 'loginmodal',
      title: 'Login to ColonialHeritage.org',
      width: '500px',
    }); // LoadModal
  }); // Click
}); // Ready
