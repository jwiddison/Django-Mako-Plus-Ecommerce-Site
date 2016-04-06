$(".big_icon").click(function() {
    $('html, body').animate({
        scrollTop: $("#link_to_form").offset().top
    }, 100000);
});
