alien = game.create_sprite(randint(0, 4), 0)
ship = game.create_sprite(2, 4)
game.set_score(0)
interval = 0

def onEvery_interval():
    alien.move(1)
    alien.if_on_edge_bounce()
    if bullet:
        if bullet.is_touching(alien)
            game.add_score(1)
            delete.bullet ()
loops.every_interval(interval, onEvery_interval)

