const characters = {
    'Kelsey' : './src/img/characters/kelsey.png',
    'J.P' : './src/img/characters/jp.png',
    'Craig' : './src/img/characters/Craig-8.png',
    'David' : './src/img/characters/David-8.png',
    'Omar' : './src/img/characters/Omar-8.png',
    'Mark' : './src/img/characters/Mark-8.png'
}

$('scroll-page').click((e)=>{
    let id = e.target.id
    $('.character .name p').text(id)
    $('.button').text(id)
    if (id in characters) $('.character img').attr({src:characters[id]})
})