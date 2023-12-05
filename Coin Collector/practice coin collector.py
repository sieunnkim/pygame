import pgzrun
from random import randint
WIDTH=400
HEIGHT=400
score = 0
game_over = False
fox= Actor("fox")
coin = Actor("coin")
fox.pos=(100,100)
coin.pos=(200,200)
timeleft=10
def draw():
  screen.fill("darkgreen")
  fox.draw()
  coin.draw()
  screen.draw.text("Score:" + str(score), topleft=(10,10))
  screen.draw.text("Time left:"+str(timeleft),topleft=(10,27))
  if game_over:
    screen.fill("black")
    screen.draw.text("Final Score:"+str(score), topleft=(10,10), fontsize=60)
def place_coin():
  coin.x=randint(20,380)
  coin.y=randint(20,380)
def update():
  if keyboard.left:
    fox.x = fox.x-2
  if keyboard.right:
    fox.x = fox.x+2
  if keyboard.up:
    fox.y = fox.y-2
  if keyboard.down:
    fox.y = fox.y+2
  global score
  if fox.colliderect(coin):
    score = score + 1
    place_coin()
def update_timeleft():
    global timeleft
    if timeleft:
        timeleft=timeleft - 1
    else:
        global game_over
        game_over=True
clock.schedule_interval(update_timeleft,1.0)
place_coin()

pgzrun.go()
