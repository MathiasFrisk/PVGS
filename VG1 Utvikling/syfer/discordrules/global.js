$(function() {
    particlesJS("particles-js", {
        "particles": {
            "number": {
                "value": 1000,
                "density": {
                    "enable": true,
                    "value_area": 3000
                }
            },
            "color": {
                "value": "#e22d2d"
            },
            "shape": {
                "type": "circle",
                "stroke": {
                    "width": 0,
                    "color": "#000000"
                },
                "polygon": {
                    "nb_sides": 3
                },
                "image": {
                    "src": "img/github.svg",
                    "width": 100,
                    "height": 100
                }
            },
            "opacity": {
                "value": 0.5,
                "random": true,
                "anim": {
                    "enable": false,
                    "speed": 1,
                    "opacity_min": 0.1,
                    "sync": false
                }
            },
            "size": {
                "value": 2,
                "random": true,
                "anim": {
                    "enable": true,
                    "speed": 5,
                    "size_min": 0,
                    "sync": false
                }
            },
            "line_linked": {
                "enable": false,
                "distance": 500,
                "color": "#ffffff",
                "opacity": 0.4,
                "width": 2
            },
            "move": {
                "enable": true,
                "speed": 3,
                "direction": "top",
                "random": true,
                "straight": false,
                "out_mode": "out",
                "bounce": false,
                "attract": {
                    "enable": false,
                    "rotateX": 600,
                    "rotateY": 1200
                }
            }
        },
        "interactivity": {
            "detect_on": "canvas",
            "events": {
                "onhover": {
                    "enable": false,
                    "mode": "bubble"
                },
                "onclick": {
                    "enable": false,
                    "mode": "repulse"
                },
                "resize": true
            },
            "modes": {
                "grab": {
                    "distance": 400,
                    "line_linked": {
                        "opacity": 0.5
                    }
                },
                "bubble": {
                    "distance": 400,
                    "size": 4,
                    "duration": 0.3,
                    "opacity": 1,
                    "speed": 3
                },
                "repulse": {
                    "distance": 200,
                    "duration": 0.4
                },
                "push": {
                    "particles_nb": 4
                },
                "remove": {
                    "particles_nb": 2
                }
            }
        },
        "retina_detect": true
    });
    
    $('.social-button').click(function() {
        if ($(this).css('left') == '-315px') {
            $(this).animate({
                left: '0px'
            }, {
                queue: false,
                duration: 500
            });
        } else {
            $(this).animate({
                left: '-315px'
            }, {
                queue: false,
                duration: 500
            });
        }
    });
    
    $('.staff-sticky-nav .goto-button').click(function () {
        var id = $(this).attr('goto');
        $('html, body').animate({
            scrollTop: $(id).offset().top - 90
        }, 500);
    });
    
    $('.menubar .items').attr('data', 'closed');
    $('.menubar .nav-open-btn a').click(function (event) {
        event.preventDefault();
        
        if ($('.menubar .items').attr('data') === 'closed') {
            $('.menubar .items').show().attr('data', 'open');
        } else {
            $('.menubar .items').hide().attr('data', 'closed');
        }
    });
    
    $('div[data = "search-user"]').click(function () {
        var input = $('input[data = "search-user-input"]').val();
        if (input !== '')
            window.location.href = Site.url + '/user/' + input;
    });
    
    $('input[data = "search-user-input"]').bind('keyup', function (event) {
        if (event.keyCode === 13) {
            var input = $(this).val();
            if (input !== '')
                window.location.href = Site.url + '/user/' + input;
        }
    });

//YOUTUBE LINKS HERE
//YOUTUBE LINKS HERE
//YOUTUBE LINKS HERE
//YOUTUBE LINKS HERE
//YOUTUBE LINKS HERE

    $(".link-twitter").click(function(){
    window.open('https://twitter.com/SpirexMC', '_blank');
    });

    $(".link-discord").click(function(){
    window.open('https://discord.spirexmc.com', '_blank');
    });

    $(".link-solyze").click(function(){
    window.open('https://www.youtube.com/channel/UCsFefJf5oCfexoNRtjWzV6g', '_blank');
    });

    $(".link-s0lrike").click(function(){
    window.open('https://www.youtube.com/channel/UCjcrU4Kbichi-_6xwmZlMtQ', '_blank');
    });
    
    if (window.location.pathname.substr(1) == 'staff') {
        var staff_sticky_nav_offset = $('.staff-sticky-nav').offset().top;
        $(window).scroll(function () {
            if ($(document).scrollTop() > (staff_sticky_nav_offset - 90)) {
                $('.staff-sticky-nav').addClass('sticky');
            } else {
                $('.staff-sticky-nav').removeClass('sticky');
            }
        });
    }

    $('.component .server-dropdown').attr('state', 'closed');
    $('.component[data]').click(function (event) {
        var name = '.component .server-dropdown[data = "'+ $(this).attr('data') +'"]';

	if ($(name).attr('state') === 'closed') {
            $(name).show().attr('state', 'open');
	    $(this).find('.icon i').removeClass('fa-plus-square').addClass('fa-minus-square');
        } else {
            $(name).hide().attr('state', 'closed');
	    $(this).find('.icon i').removeClass('fa-minus-square').addClass('fa-plus-square');
        }
    });
});

function updateServerStatus () {
    $.post(Site.url +'/home/status/load', function (json) {
	for (var data in json.servers) {
	    if (json.servers[data].servers != null) {
		for (var data2 in json.servers[data].servers) {
		    $('#'+ json.servers[data].name +'-'+ json.servers[data].servers[data2].name).html(json.servers[data].servers[data2].status);
		}
	    } else {
		$('#'+ json.servers[data].name).html(json.servers[data].status);
	    }
	}
    });

    setTimeout(updateServerStatus, 60000);
}

function initializeNetworkData () {
    MinecraftAPI.getServerStatus(Site.serverip, function (err, status) {
        if (status.online) {
            $('.networkstatus').html('Join us at <span class="important">'+ Site.serverip +'</span> and play with <span class="important">'+ status.players.now +'</span> other players!');
        } else {
            $('.networkstatus').html('The network is currently offline. We will be back soon!');
        }
    });
    
    setTimeout(initializeNetworkData, 5000);
}

function initializeDiscordData () {
    $.getJSON(External.discord_embed, function (json) {
        $('.discord-users').html('Currently <b>'+ json.presence_count +'</b> Discord users online');
    });
    
    setTimeout(initializeDiscordData, 60000);
}

if (true) {
    updateServerStatus();
}

initializeNetworkData();
initializeDiscordData();