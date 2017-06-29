$(document).ready(function() {
    $(document).on("click", ".arrow-menu", function (e) {
            console.log('fuck');
            if ($('.menu').hasClass('visible-md', 'visible-lg')){
                $('.menu').removeClass('visible-md', 'visible-lg').slideDown();
            }
            else{
                $('.menu').addClass('visible-md', 'visible-lg').slideUp();
            }
        });
//    Это наше верхнее меню на телефоне !!!!!!!!!!!
    var delay = 1000; // Задержка прокрутки
    $(window).scroll(function () {
          if ($(this).scrollTop() > 100) {
              console.log('dd');
              $('.top-mob').addClass('fixed-menu-arr');
              $('.menu').addClass('fixed-menu');
          }
          else if ($(this).scrollTop() < 100) {
              $('.top-mob').removeClass('fixed-menu-arr');
              $('.menu').removeClass('fixed-menu');

          }
          if ($(this).scrollTop() > 200) $('#top').fadeIn();
          else $('#top').fadeOut();
    });
    $('#top').click(function () { // При клике по кнопке "Наверх" попадаем в эту функцию
        /* Плавная прокрутка наверх */
        $('body, html').animate({scrollTop: 0}, delay);
    });
    $('#feed').submit(function (e) {
             console.log('aa');
            e.preventDefault();
            // console.log();
            $.ajax({
                url: '/mass/',
                type: 'POST',
                data: $('#feed').serialize(),
                success: function (data) {
                    var html = "";
                    $('.modal-body').empty();
                    $.each(data, function (index, data){
                        html += '<div class="text-center" style="font-size: 16px" '
                        + '<p>'
                        + data.text_data
                        + '</p>'
                        + '</div>';
                    });
                    $('.modal-body').append(html);
                }
            });
        });
        $('#contact').submit(function (e) {
             console.log('aa');
            e.preventDefault();
            console.log(window.location.href);
            $.ajax({
                url: '/massgen/',
                type: 'POST',
                data: $('#contact').serialize(),
                success: function (data) {
                    var html = "";
                    $('.call-back-text').empty();
                    $('.call-back-text').css({"background": "rgba(8, 100, 255, 0.6)",'color': 'white'});
                    $.each(data, function (index, data){
                        html += data.text_data;
                    });
                    $('.call-back-text').append(html);
                }
            });
        });

});