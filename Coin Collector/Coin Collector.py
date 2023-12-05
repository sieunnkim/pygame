import pgzrun
from random import randint
WIDTH = 400
HEIGHT= 400
score = 0
game_over= False
fox = Actor("fox")
fox.pos = 100,100
coin = Actor("coin")
coin.pos = 200, 200
def draw():
    screen.fill("darkgreen")
    fox.draw()
    coin.draw()
    screen.draw.text("Score:"+str(score),color="black",topleft=(10,10))
    if game_over:
        screen.fill("beige")
        screen.draw.text("Final Score:"+str(score),color=(34,47,85), topleft=(10,10), fontsize=60)
def place_coin():
    coin.x=randint(20,(WIDTH-20))
    coin.y=randint(20,(HEIGHT-20))
def time_up():
    global game_over
    game_over = True
def update():
    if keyboard.left:
        fox.x = fox.x - 2
    if keyboard.right:
        fox.x = fox.x + 2
    if keyboard.up:
        fox.y = fox.y - 2
    if keyboard.down:
        fox.y = fox.y + 2
    global score
    coin_collected = fox.colliderect(coin)
    if coin_collected:
        score = score+10
        place_coin()

clock.schedule(time_up,10.0)
place_coin()


pgzrun.go()

