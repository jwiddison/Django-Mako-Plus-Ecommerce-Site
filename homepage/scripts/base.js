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

$(function() {
  $('#delete_button').click(function() {
    $.loadmodal({
      url: '/manager/users.delete/',
      id: 'delete_modal',
      title: 'Are you sure?',
      width: '500px',
    }); // LoadModal
  }); // Click
}); // Ready
