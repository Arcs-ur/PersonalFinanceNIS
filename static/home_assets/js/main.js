"use strict";
jQuery( document ).ready( function ( $ ) {

//for Preloader

    $( window ).load( function () {
        $( ".loaderbox" ).fadeOut();
        $( ".preloader" ).delay( 1000 ).fadeOut( "slow" );
    } );


    /*---------------------------------------------*
     * Mobile menu
     ---------------------------------------------*/
    $( '.navbar-collapse' ).find( 'a[href*=#]:not([href=#])' ).click( function () {
        if ( location.pathname.replace( /^\//, '' ) == this.pathname.replace( /^\//, '' ) && location.hostname == this.hostname ) {
            var target = $( this.hash );
            target = target.length ? target : $( '[name=' + this.hash.slice( 1 ) + ']' );
            if ( target.length ) {
                $( 'html,body' ).animate( {
                    scrollTop: ( target.offset().top - 30 )
                }, 1000 );
                if ( $( '.navbar-toggle' ).css( 'display' ) != 'none' ) {
                    $( this ).parents( '.container' ).find( ".navbar-toggle" ).trigger( "click" );
                }
                return false;
            }
        }
    } );

    /*============================================*
     * home v1 slider
     =============================================*/

    $( '#bootstrap-touch-slider' ).bsTouchSlider();


    /*=============================================*
     * WOW
     ==============================================*/

    var wow = new WOW( {
        mobile: false // trigger animations on mobile devices (default is true)
    } );
    wow.init();


// magnificPopup

    $( '.popup-img' ).magnificPopup( {
        type: 'image',
        gallery: {
            enabled: true
        }
    } );
    $( '.video-link' ).magnificPopup( {
        type: 'iframe'
    } );



// Carousel slider 

    $( '.carousel' ).each( function () {
        $( this ).carousel( {
            pause: true,
            interval: false
        } );
    } );


//---------------------------------------------
// Counter 
//---------------------------------------------

    $( '.statistic-counter' ).counterUp( {
        delay: 10,
        time: 2000
    } );


//---------------------------------------------
// Scroll Up 
//---------------------------------------------

    $( '.scrollup' ).click( function () {
        $( "html, body" ).animate( { scrollTop: 0 }, 1000 );
        return false;
    } );


//  Mixitup Portfolio

    $( '.main-work' ).mixItUp( {
        animation: {
            effects: 'fade translateX(50%)',
            reverseOut: true,
            duration: 1000
        },
        load: {
            filter: 'all'
        }
    } );

//Team Skillbar active js


    jQuery( '.border' ).parent( 'div' ).addClass( 'parent-border' );

    jQuery( '#newsletter-form' ).formchimp( { 'buttonText': 'Thanks' } );




//main newes blog slider
    $( ".main-newest-blog" ).slick( {
        dots: true,
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        arrows: true,
        prevArrow: "<i class='icon icon-arrows-3 nextprevleft'></i>",
        nextArrow: "<i class='icon icon-arrows-2 nextprevright'></i>",
//        autoplay: true,
        autoplaySpeed: 2000,
        responsive: [
            {
                breakpoint: 991,
                settings: {
                    arrows: false,
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 768,
                settings: {
                    autoplay: true,
//                    dots: false,
                    arrows: false,
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    } );


    jQuery( '.main-studies' ).imagesLoaded( function () {} );





    var controller = new ScrollMagic.Controller();

    new ScrollMagic.Scene( { triggerElement: ".clients" } )
        .setVelocity( ".transit-01", { bottom: "10%" }, 600 ).addTo( controller );

    new ScrollMagic.Scene( { triggerElement: ".clients" } )
        .setVelocity( ".transit-02", { bottom: "10%" }, 600 ).addTo( controller );

    new ScrollMagic.Scene( { triggerElement: ".localseo" } )
        .setVelocity( ".transit-03", { top: "26%" }, 600 ).addTo( controller );

    new ScrollMagic.Scene( { triggerElement: ".localseo" } )
        .setVelocity( ".transit-04", { left: "1%" }, 700 ).addTo( controller );

    new ScrollMagic.Scene( { triggerElement: ".localseo" } )
        .setVelocity( ".transit-05", { top: "28%" }, 600 ).addTo( controller );

    new ScrollMagic.Scene( { triggerElement: ".localseo" } )
        .setVelocity( ".transit-06", { right: "0%" }, 700 ).addTo( controller );

    new ScrollMagic.Scene( { triggerElement: ".localseo-hv2" } )
        .setVelocity( ".transit-07", { bottom: "0%" }, 600 ).addTo( controller );

    new ScrollMagic.Scene( { triggerElement: ".localseo-hv2" } )
        .setVelocity( ".transit-08", { bottom: "0%" }, 600 ).addTo( controller );




// nav menu
    $( document ).on( "scroll", function () {
        if ( $( document ).scrollTop() > 0 ) {
            $( "nav" ).addClass( "scroll_menu" );
        } else {
            $( "nav" ).removeClass( "scroll_menu" );
        }
    } );



    //End

} );












