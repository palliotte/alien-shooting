let alien = game.createSprite(randint(0, 4), 0)
let ship = game.createSprite(2, 4)
game.setScore(0)
let interval = 0
loops.everyInterval(interval, function onEvery_interval() {
    alien.move(1)
    alien.ifOnEdgeBounce()
})
