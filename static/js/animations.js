/**
 * Advanced jQuery Animation and Interaction Library
 * For Advit Placement Services - Pixel Perfect Animations
 */

$(document).ready(function() {
    
    /* ========== SMOOTH PAGE TRANSITIONS ========== */
    // Fade in elements on page load
    $(document).ready(function() {
        $('.fade-in').each(function(index) {
            $(this).css('opacity', '0');
            $(this).delay(index * 100).animate({ opacity: 1 }, 500);
        });
    });
    
    /* ========== NAVBAR SCROLL EFFECTS ========== */
    var navbar = $('.navbar');
    var lastScrollTop = 0;
    
    $(window).scroll(function() {
        var st = $(this).scrollTop();
        
        if (st > 100) {
            navbar.addClass('scrolled');
            navbar.css('box-shadow', '0 4px 20px rgba(0,0,0,0.3)');
        } else {
            navbar.removeClass('scrolled');
            navbar.css('box-shadow', '0 8px 32px rgba(0,0,0,0.2)');
        }
        
        lastScrollTop = st;
    });
    
    /* ========== SMOOTH SCROLL ANCHOR LINKS ========== */
    $('a[href^="#"]').on('click', function(e) {
        e.preventDefault();
        var target = $(this.getAttribute('href'));
        if(target.length) {
            $('html, body').stop().animate({
                scrollTop: target.offset().top - 60
            }, 1000, 'easeInOutQuad');
        }
    });
    
    /* ========== CARD HOVER 3D EFFECT ========== */
    $('.card').on('mousemove', function(e) {
        var card = $(this);
        var rect = this.getBoundingClientRect();
        var x = e.clientX - rect.left;
        var y = e.clientY - rect.top;
        
        var xRotation = ((y - rect.height / 2) / rect.height) * 10;
        var yRotation = ((x - rect.width / 2) / rect.width) * 10;
        
        card.css({
            'transform': 'perspective(1000px) rotateX(' + xRotation + 'deg) rotateY(' + yRotation + 'deg) translateZ(20px)',
            'transition': 'none'
        });
    }).on('mouseleave', function() {
        $(this).css({
            'transform': 'perspective(1000px) rotateX(0) rotateY(0) translateZ(0)',
            'transition': 'all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1)'
        });
    });
    
    /* ========== BUTTON RIPPLE EFFECT ========== */
    $('.btn').on('click', function(e) {
        var ripple = $('<span class="ripple"></span>');
        var rect = this.getBoundingClientRect();
        var size = Math.max(rect.width, rect.height);
        var x = e.clientX - rect.left - size / 2;
        var y = e.clientY - rect.top - size / 2;
        
        ripple.css({
            'width': size,
            'height': size,
            'left': x,
            'top': y
        });
        
        $(this).append(ripple);
        
        setTimeout(function() {
            ripple.remove();
        }, 600);
    });
    
    // Add ripple CSS dynamically
    if (!$('#ripple-style').length) {
        $('<style id="ripple-style">' +
            '.btn { position: relative; overflow: hidden; }' +
            '.ripple { position: absolute; border-radius: 50%; background: rgba(255,255,255,0.5); transform: scale(0); animation: rippleEffect 0.6s ease-out; }' +
            '@keyframes rippleEffect { to { transform: scale(4); opacity: 0; } }' +
            '</style>').appendTo('head');
    }
    
    /* ========== PARALLAX SCROLL EFFECT ========== */
    $(window).scroll(function() {
        var scrollPercent = $(window).scrollTop() / ($(document).height() - $(window).height());
        
        $('.parallax-bg').css({
            'transform': 'translateY(' + (scrollPercent * 50) + 'px)'
        });
        
        // 3D rotation effect for hero section
        var heroRotation = scrollPercent * 5;
        $('.jumbotron').css({
            'transform': 'perspective(1200px) rotateX(' + heroRotation + 'deg) translateY(' + (scrollPercent * 20) + 'px)'
        });
    });
    
    /* ========== STAGGERED ELEMENT ANIMATIONS ========== */
    function animateElementsOnScroll() {
        var elements = $('.slide-in-left, .slide-in-right');
        
        elements.each(function() {
            var elementTop = $(this).offset().top;
            var elementBottom = elementTop + $(this).outerHeight();
            var viewportTop = $(window).scrollTop();
            var viewportBottom = viewportTop + $(window).height();
            
            if (elementBottom > viewportTop && elementTop < viewportBottom) {
                $(this).addClass('in-view');
            }
        });
    }
    
    $(window).scroll(animateElementsOnScroll);
    animateElementsOnScroll(); // Run on page load
    
    /* ========== FORM INPUT ANIMATION ========== */
    $('.form-control').on('focus', function() {
        $(this).closest('.form-group').addClass('active');
        $(this).css({
            'transform': 'translateY(-2px)',
            'box-shadow': '0 8px 16px rgba(0,123,255,0.15)'
        });
    }).on('blur', function() {
        if(!$(this).val()) {
            $(this).closest('.form-group').removeClass('active');
        }
        $(this).css({
            'transform': 'translateY(0)',
            'box-shadow': '0 0 0 0.3rem rgba(0,123,255,0.0)'
        });
    });
    
    /* ========== COUNTER ANIMATION ========== */
    function animateCounter(element, target, duration = 2000) {
        var current = parseInt($(element).text()) || 0;
        var increment = target / (duration / 16);
        var timer = setInterval(function() {
            current += increment;
            if(current >= target) {
                $(element).text(Math.floor(target));
                clearInterval(timer);
            } else {
                $(element).text(Math.floor(current));
            }
        }, 16);
    }
    
    // Animate counters when they come into view
    $('.counter').each(function() {
        var target = parseInt($(this).data('target'));
        var self = this;
        
        var observer = new IntersectionObserver(function(entries) {
            if(entries[0].isIntersecting) {
                animateCounter(self, target);
                observer.unobserve(self);
            }
        });
        
        observer.observe(this);
    });
    
    /* ========== DROPDOWN ANIMATION ========== */
    $('.dropdown-toggle').on('click', function() {
        $(this).closest('.dropdown').find('.dropdown-menu').slideToggle(300);
    });
    
    /* ========== ALERT AUTO-CLOSE ========== */
    $('.alert').each(function() {
        var alert = $(this);
        setTimeout(function() {
            alert.fadeOut(300, function() {
                $(this).remove();
            });
        }, 5000);
    });
    
    /* ========== LAZY LOAD IMAGES ========== */
    if ('IntersectionObserver' in window) {
        var imageObserver = new IntersectionObserver(function(entries, observer) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    var img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.add('loaded');
                    observer.unobserve(img);
                }
            });
        });
        
        document.querySelectorAll('img[data-src]').forEach(img => imageObserver.observe(img));
    }
    
    /* ========== FLOATING ANIMATION FOR ELEMENTS ========== */
    function createFloatingAnimation() {
        var keyframes = `
            @keyframes floatingSmall {
                0%, 100% { transform: translateY(0px); }
                50% { transform: translateY(-10px); }
            }
            @keyframes floatingMedium {
                0%, 100% { transform: translateY(0px); }
                50% { transform: translateY(-15px); }
            }
            @keyframes floatingLarge {
                0%, 100% { transform: translateY(0px); }
                50% { transform: translateY(-20px); }
            }
        `;
        
        var style = document.createElement('style');
        style.textContent = keyframes;
        document.head.appendChild(style);
        
        $('.floating').each(function(index) {
            var animations = ['floatingSmall', 'floatingMedium', 'floatingLarge'];
            var animation = animations[index % animations.length];
            $(this).css({
                'animation': animation + ' ' + (3 + index * 0.5) + 's ease-in-out infinite'
            });
        });
    }
    
    createFloatingAnimation();
    
    /* ========== SCROLL PROGRESS INDICATOR ========== */
    var progressBar = $('<div class="scroll-progress"></div>');
    progressBar.css({
        'position': 'fixed',
        'top': '0',
        'left': '0',
        'height': '3px',
        'background': 'linear-gradient(90deg, #007bff, #23d5ab)',
        'width': '0%',
        'z-index': '9999',
        'transition': 'width 0.3s ease'
    });
    $('body').append(progressBar);
    
    $(window).scroll(function() {
        var windowheight = $(document).height() - $(window).height();
        var scrollPercent = $(window).scrollTop() / windowheight * 100;
        progressBar.css('width', scrollPercent + '%');
    });
    
    /* ========== TOOLTIP INITIALIZATION ========== */
    $('[data-toggle="tooltip"]').each(function() {
        var tooltip = $('<div class="tooltip-custom"></div>');
        tooltip.text($(this).data('title'));
        tooltip.css({
            'position': 'absolute',
            'background': 'rgba(0,0,0,0.8)',
            'color': 'white',
            'padding': '5px 10px',
            'border-radius': '5px',
            'font-size': '12px',
            'white-space': 'nowrap',
            'pointer-events': 'none',
            'z-index': '9999',
            'display': 'none'
        });
        
        $('body').append(tooltip);
        
        $(this).on('mouseenter', function(e) {
            tooltip.css({
                'left': e.pageX + 10,
                'top': e.pageY + 10,
                'display': 'block'
            }).fadeIn(200);
        }).on('mouseleave', function() {
            tooltip.fadeOut(200);
        });
    });
    
    /* ========== NOTIFICATION SYSTEM ========== */
    window.notify = function(message, type = 'info', duration = 4000) {
        var notification = $('<div class="notification notification-' + type + '">' + message + '</div>');
        notification.css({
            'position': 'fixed',
            'top': '20px',
            'right': '20px',
            'padding': '15px 20px',
            'border-radius': '5px',
            'color': 'white',
            'z-index': '9999',
            'animation': 'slideInRight 0.3s ease-out',
            'box-shadow': '0 4px 12px rgba(0,0,0,0.15)'
        });
        
        var bgColor = {
            'success': '#28a745',
            'error': '#dc3545',
            'warning': '#ffc107',
            'info': '#17a2b8'
        };
        
        notification.css('background', bgColor[type] || bgColor['info']);
        $('body').append(notification);
        
        setTimeout(function() {
            notification.fadeOut(300, function() {
                $(this).remove();
            });
        }, duration);
    };
    
    /* ========== SMOOTH HOVER TEXT EFFECT ========== */
    $('.hover-text').on('mouseenter', function() {
        $(this).css({
            'transform': 'scale(1.05)',
            'color': '#23d5ab'
        });
    }).on('mouseleave', function() {
        $(this).css({
            'transform': 'scale(1)',
            'color': 'inherit'
        });
    });
    
    /* ========== INTERSECTION OBSERVER FOR FADE IN ========== */
    if ('IntersectionObserver' in window) {
        var observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    $(entry.target).addClass('fade-in-view');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);
        
        $('.card, .job-card, .company-card').each(function() {
            observer.observe(this);
        });
    }
    
    /* ========== KEYBOARD ACCESSIBILITY ========== */
    $(document).on('keydown', function(e) {
        // Escape key closes modals
        if(e.keyCode === 27) {
            $('.modal').fadeOut();
        }
        // Tab navigation enhancement
        if(e.keyCode === 9) {
            $(document.activeElement).css('outline', '2px solid #007bff');
        }
    });
});

// jQuery easing extension for smooth animations
jQuery.easing.easeInOutQuad = function(x, t, b, c, d) {
    if ((t/=d/2) < 1) return c/2*t*t + b;
    return -c/2 * ((--t)*(t-2) - 1) + b;
};
