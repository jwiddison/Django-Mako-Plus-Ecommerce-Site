$('.stripe_button').click(function(event){
  if !(('#verify_checkbox').checked){
    console.log('Test');
    event.preventDefault();
  }
}
