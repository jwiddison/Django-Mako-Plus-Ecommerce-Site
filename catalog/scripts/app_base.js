// $(function() {
//     var theLoc = $('#fixed_left').position().top;
//     $(window).scroll(function() {
//         if(theLoc >= $(window).scrollTop()) {
//             if($('#fixed_left').hasClass('fixed')) {
//                 $('#fixed_left').removeClass('fixed');
//             }
//         } else {
//             if(!$('#fixed_left').hasClass('fixed')) {
//                 $('#fixed_left').addClass('fixed');
//             }
//         }
//     });
//     var theLoc2 = $('#fixed_right').position().top;
//     $(window).scroll(function() {
//         if(theLoc2 >= $(window).scrollTop()) {
//             if($('#fixed_right').hasClass('fixed')) {
//                 $('#fixed_right').removeClass('fixed');
//             }
//         } else {
//             if(!$('#fixed_right').hasClass('fixed')) {
//                 $('#fixed_right').addClass('fixed');
//             }
//         }
//     });
// }); //ready

// $.fn.followTo = function (pos) {
//     var $this = this,
//         $window = $(window);
//
//     $window.scroll(function (e) {
//         if ($window.scrollTop() > pos) {
//             $this.css({
//                 position: 'absolute',
//                 top: pos
//             });
//         } else {
//             $this.css({
//                 position: 'fixed',
//                 top: 0
//             });
//         }
//     });
// };
//
// $('#fixed_left').followTo(250);
// $('#fixed_right').followTo(250);
