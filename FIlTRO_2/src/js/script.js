const info = [
{
    temporada_n: 1,
    info_temp : {
        c_capitulos : 7,
        i_capitulos : {
            1 : {
                src : "./src/img/temp_1/cap1.png",
                color : "#8FD9A9",
                styles : {
                    bg: 'url("http://drive.google.com/uc?export=view&id=1FzvApGj6j3k5zU_4V0zvO-O3jSzYMe2d")',
                    drop : "#8FD9A9",
                    cap: 'ITCH TO EXPLORE'
                }
            },
            2: {
                src : "./src/img/temp_1/cap2.png",
                color : "#D9D2AD",
                styles : {
                    bg: 'url("http://drive.google.com/uc?export=view&id=1hVi3pg7BAy14UZ1mZI3gEMoyjwgeGWCJ")',
                    drop : '#242040',
                    cap : 'JACOB OF THE CREEK'
                }
            },
            3 : {
                src : "./src/img/temp_1/cap3.png",
                color : "#D3B2FE",
                styles : {
                    bg :'url("http://drive.google.com/uc?export=view&id=1tOthEPd4iTUEzLaNXk_m92fOYeGIgctn")',
                    drop : '#F2B988',
                    cap : "YOU'RE IT"
                }
            },
            4: {
                src : "./src/img/temp_1/cap4.png",
                color : "#6970CA",
                styles : {
                    bg: 'url("http://drive.google.com/uc?export=view&id=1beegSynd4pdMN2_xF4A6yQASktTFLm2h")',
                    drop : '#5A4BBF',
                    cap : 'THE CURSE'
                }
            },
            5 : {
                src : "./src/img/temp_1/cap5.png",
                color : "#D3B2FE",
                styles : {
                    bg: 'url("http://drive.google.com/uc?export=view&id=1u0jDTqWGe2KYVnTcuCbWPwS3PskZBqBV")',
                    drop : '#403F59',
                    cap : 'POWER PUNCHERS'
                }
            },
            6 : {
                src : "./src/img/temp_1/cap6.png",
                color : "#D3B2FE",
                styles : {
                    bg: 'url("http://drive.google.com/uc?export=view&id=1cWjFfqVdbvAWxDz6PUHJXNxdZh9NEAMf")',
                    drop : '#70736A',
                    cap : 'SECRET BOOK CLUB'
                }
            },
            7 : {
                src : "./src/img/temp_1/cap7.png",
                color : "#D3B2FE",
                styles : {
                    bg: 'url("http://drive.google.com/uc?export=view&id=1RCTpYBfSvBwmIRk0AbGWUmPbzR6vFHCp")',
                    drop : '#730202',
                    cap : 'DIBS COURT'
                }
            }
        }
    }
},
{
    temporada_n: 2,
    info_temp : {
        c_capitulos : 5,
        i_capitulos : {
            1 : {
                src : "./src/img/temp_2/cap1.png",
                color : "#D3B2FE",
                styles : {
                    bg: 'url("http://drive.google.com/uc?export=view&id=1w4BxgyshE34PM73LFo49IXH-fE2NurMA")',
                    drop : '#BF6C3B',
                    cap : 'HONEY SUCKLE RANGERS'
                }
            },
            2: {
                src : "./src/img/temp_2/cap2.png",
                color : "#D3B2FE",
                styles : {
                    bg: 'url("http://drive.google.com/uc?export=view&id=1Yv-eMX9hHmyv3_R7UiJWFOUopJ2eVeR1")',
                    drop : '#8DA668',
                    cap : 'KELSEY THE ELDER'
                }
            },
            3 : {
                src : "./src/img/temp_2/cap3.png",
                color : "#D3B2FE",
                styles : {
                    bg: 'url("http://drive.google.com/uc?export=view&id=10l8ozAMomovUxVeSvxscBIFhE-zoxx8f")',
                    drop : '#56BFBF',
                    cap : 'THE HAUNTED DOLLHOUSE'
                }
            },
            4: {
                src : "./src/img/temp_2/cap4.png",
                color : "#D3B2FE",
                styles : {
                    bg: 'url("http://drive.google.com/uc?export=view&id=1OLemivOiDByw1uJCCPsO8kn4-0Ebf7Sg")',
                    drop : '#4A2D73',
                    cap : 'SUGAR SMUGGLERS'
                }
            },
            5 : {
                src : "./src/img/temp_2/cap5.png",
                color : "#D3B2FE",
                styles : {
                    bg: 'url("http://drive.google.com/uc?export=view&id=1tRikuwk1WTU3Tk-hyt7kjPiq5RYHoW0r")',
                    drop : '#736E30',
                    cap : 'CRISIS AT ELDER ROCK'
                }
            }
        }
    }
}]

// Creaacion de las portadas

function loadChapters (nt) {
    for(var i=1; i<=info[nt].info_temp.c_capitulos; i++){
        var span = $("<span></span>").text(i<10 ? '0'+i.toString() : i.toString()) // Creacion del numero del capitulo
        span.css('color',info[nt].info_temp.i_capitulos[i].color) // Color num
        var img = $("<img>").attr({id: i, class: 'item',src:info[nt].info_temp.i_capitulos[i].src}) // Creacion imagen portada
        var scroll_page = $("<scroll-page></scroll-page>").append(span, img) // Creacion del scroll.page y agrego span e imagen
        $('scroll-container').append(scroll_page) // Agrego scroll-page a scroll-container
    }
}



function clear () {
    const scrolls = document.querySelectorAll('scroll-page')
    scrolls.forEach(scroll => {
        scroll.remove()
    })
}

function change(nt) {
    $('scroll-page img').hover( (e) => {
        let id = e.target.id<=info[nt].info_temp.c_capitulos ? e.target.id : 1;
        let int_id = parseInt(id)
        let style = info[nt].info_temp.i_capitulos[id].styles
        console.log(style.bg)
        $('body').css('background-image', style.bg);
        $('.info').css('color', style.drop);
        $('.play_button .circle-bg').css('background-color', style.drop);
        $('.play_button a').css('color', style.drop);
        $('.select').css('color', style.drop);
        $(':root').css('--scroll-color', style.drop)
        $('.snif').text(int_id<10 ? '0'+id : id);
        $('.name-cap').text(style.cap);
        $('.menu-bar').css('color', style.drop)
    })
}


$(document).ready (() => {

    loadChapters(0)

    change(0)

    const dropdowns = document.querySelectorAll('.dropdown');
    dropdowns.forEach(dropdown => {
        const options = dropdown.querySelectorAll('.menu li');
        const selected = dropdown.querySelector('.selected') 

        $('.select').click(()=>{
            $('.select').addClass('select-clicked');
            $('.caret').addClass('caret-rotate');
            $('.menu').addClass('menu-open')
        });

        options.forEach(option => {
            option.addEventListener('click', (e)=>{
                clear()
                loadChapters(parseInt(e.target.id))
                change(parseInt(e.target.id))
                selected.innerText = option.innerText
                $('.select').removeClass('select-clicked')
                $('.caret').removeClass('caret-rotate')
                $('.menu').removeClass('menu-open')

                options.forEach(option => {
                    option.classList.remove('active')
                })
                option.classList.add('active')
            })
        })

    })
})

