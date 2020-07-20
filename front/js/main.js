(function ($) {
  "use strict";

  // Preloader (if the #preloader div exists)
  $(window).on('load', function () {
    if ($('#preloader').length) {
      $('#preloader').delay(100).fadeOut('slow', function () {
        $(this).remove();
      });
    }
  });

  // Back to top button
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      $('.back-to-top').fadeIn('slow');
    } else {
      $('.back-to-top').fadeOut('slow');
    }
  });
  $('.back-to-top').click(function(){
    $('html, body').animate({scrollTop : 0},1500, 'easeInOutExpo');
    return false;
  });

  // Initiate the wowjs animation library
  new WOW().init();

  // Header scroll class
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      $('#header').addClass('header-scrolled');
    } else {
      $('#header').removeClass('header-scrolled');
    }
  });

  if ($(window).scrollTop() > 100) {
    $('#header').addClass('header-scrolled');
  }

  // Smooth scroll for the navigation and links with .scrollto classes
  $('.main-nav a, .mobile-nav a, .scrollto').on('click', function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      if (target.length) {
        var top_space = 0;

        if ($('#header').length) {
          top_space = $('#header').outerHeight();

          if (! $('#header').hasClass('header-scrolled')) {
            top_space = top_space - 40;
          }
        }

        $('html, body').animate({
          scrollTop: target.offset().top - top_space
        }, 1500, 'easeInOutExpo');

        if ($(this).parents('.main-nav, .mobile-nav').length) {
          $('.main-nav .active, .mobile-nav .active').removeClass('active');
          $(this).closest('li').addClass('active');
        }

        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('.mobile-nav-toggle i').toggleClass('fa-times fa-bars');
          $('.mobile-nav-overly').fadeOut();
        }
        return false;
      }
    }
  });

  // Navigation active state on scroll
  var nav_sections = $('section');
  var main_nav = $('.main-nav, .mobile-nav');
  var main_nav_height = $('#header').outerHeight();

  $(window).on('scroll', function () {
    var cur_pos = $(this).scrollTop();
  
    nav_sections.each(function() {
      var top = $(this).offset().top - main_nav_height,
          bottom = top + $(this).outerHeight();
  
      if (cur_pos >= top && cur_pos <= bottom) {
        main_nav.find('li').removeClass('active');
        main_nav.find('a[href="#'+$(this).attr('id')+'"]').parent('li').addClass('active');
      }
    });
  });

  // jQuery counterUp (used in Whu Us section)
  $('[data-toggle="counter-up"]').counterUp({
    delay: 10,
    time: 1000
  });

  // Porfolio isotope and filter
  $(window).on('load', function () {

    const container = document.getElementById('tests');

    var request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:8000/api/tests/', true);
    request.onload = function () {
      // Begin accessing JSON data here
      var data = JSON.parse(this.response);
      if (request.status >= 200 && request.status < 400) {
        data.forEach(test => {
          const item = document.createElement('label');
          item.setAttribute('class', 'item');
          item.textContent = test.name;

          const checkbox = document.createElement('input');
          checkbox.setAttribute('type', 'checkbox');
          checkbox.setAttribute('name', test.id);
          const checkmark = document.createElement('span');
          checkmark.setAttribute('class', 'checkmark');

          container.appendChild(item);
          item.appendChild(checkbox);
          item.appendChild(checkmark);
        });
      } else {
        const errorMessage = document.createElement('marquee');
        errorMessage.textContent = `Gah, it's not working!`;
        app.appendChild(errorMessage);
      }
    }

    request.send();

    var portfolioIsotope = $('.portfolio-container').isotope({
      itemSelector: '.portfolio-item'
    });
    $('#portfolio-flters li').on( 'click', function() {
      $("#portfolio-flters li").removeClass('filter-active');
      $(this).addClass('filter-active');
  
      portfolioIsotope.isotope({ filter: $(this).data('filter') });
    });
  });

  // Testimonials carousel (uses the Owl Carousel library)
  $(".testimonials-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    items: 1
  });

  // Clients carousel (uses the Owl Carousel library)
  $(".clients-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    responsive: { 0: { items: 2 }, 768: { items: 4 }, 900: { items: 6 }
    }
  });

  $( "#sendTests" ).click(function() {
    var request = new XMLHttpRequest();
    var selectedTests = $('#tests input:checked');
    var str = selectedTests[0].getAttribute('name');
    for (var i = 1; i < selectedTests.length; i++) {
      str += ',' + selectedTests[i].getAttribute('name');
    }
    request.open('GET', 'http://127.0.0.1:8000/api/labs-and-prices/?tests='+str, true);
    request.onload = function () {
      // Begin accessing JSON data here
      const container = document.getElementById('labs');
      var data = JSON.parse(this.response);
      if (request.status >= 200 && request.status < 400) {
        data.forEach(lab => {
          const item = document.createElement('label');
          item.setAttribute('class', 'item');
          item.textContent = lab.name + ' (' + lab.price + 'T)';

          const radio = document.createElement('input');
          radio.setAttribute('type', 'radio');
          radio.setAttribute('name', 'lab');
          radio.setAttribute('value', lab.id);
          const checkmark = document.createElement('span');
          checkmark.setAttribute('class', 'radio');

          container.appendChild(item);
          item.appendChild(radio);
          item.appendChild(checkmark);

          $('#labSection').removeClass('hidden');
          $('#testSection').addClass('hidden');

        });
      } else {
        const errorMessage = document.createElement('marquee');
        errorMessage.textContent = `Gah, it's not working!`;
        app.appendChild(errorMessage);
      }
    }

    request.send();
  });

  $( "#getAddresses" ).click(function() {
    var request = new XMLHttpRequest();
    var selectedTests = $('#tests input:checked');
    var str = selectedTests[0].getAttribute('name');
    for (var i = 1; i < selectedTests.length; i++) {
      str += ',' + selectedTests[i].getAttribute('name');
    }
    request.open('GET', 'http://127.0.0.1:8000/api/addresses', true);
    request.onload = function () {
      // Begin accessing JSON data here
      const container = document.getElementById('addresses');
      var data = JSON.parse(this.response);
      if (request.status >= 200 && request.status < 400) {
        data.forEach(address => {
          const item = document.createElement('label');
          item.setAttribute('class', 'item');
          item.textContent = address.address;

          const radio = document.createElement('input');
          radio.setAttribute('type', 'radio');
          radio.setAttribute('name', 'address');
          radio.setAttribute('value', address.id);
          const checkmark = document.createElement('span');
          checkmark.setAttribute('class', 'radio');

          container.appendChild(item);
          item.appendChild(radio);
          item.appendChild(checkmark);

          $('#labSection').addClass('hidden');
          $('#addressSection').removeClass('hidden');
        });
      } else {
        const errorMessage = document.createElement('marquee');
        errorMessage.textContent = `Gah, it's not working!`;
        app.appendChild(errorMessage);
      }
    }

    request.send();
  });

  $( "#getTimeslots" ).click(function() {
    var request = new XMLHttpRequest();
    var selectedLab = $("input:radio[name ='lab']:checked").val();
    request.open('GET', 'http://127.0.0.1:8000/api/time-slots/?lab='+selectedLab, true);
    request.onload = function () {
      // Begin accessing JSON data here
      const container = document.getElementById('timeslots');
      var data = JSON.parse(this.response);
      if (request.status >= 200 && request.status < 400) {
        data.forEach(timeslot => {
          const item = document.createElement('label');
          item.setAttribute('class', 'item');
          item.textContent = timeslot.date;

          const radio = document.createElement('input');
          radio.setAttribute('type', 'radio');
          radio.setAttribute('name', 'timeslot');
          radio.setAttribute('value', timeslot.id);
          const checkmark = document.createElement('span');
          checkmark.setAttribute('class', 'radio');

          container.appendChild(item);
          item.appendChild(radio);
          item.appendChild(checkmark);

          $('#addressSection').addClass('hidden');
          $('#timeslotSection').removeClass('hidden');
        });
      } else {
        const errorMessage = document.createElement('marquee');
        errorMessage.textContent = `Gah, it's not working!`;
        app.appendChild(errorMessage);
      }
    }

    request.send();
  });


})(jQuery);

