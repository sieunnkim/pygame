import pgzrun
from random import randint
HEIGHT = 600
WIDTH = 800

balloon = Actor("balloon")
bird = Actor("bird-up")
house = Actor("house")
tree = Actor("tree")

balloon.pos = (400,300)
bird.pos=(randint(800,1600),randint(10,150))
house.pos=(randint(800,1600),460)
tree.pos=(randint(800,1600),450)

game_over = False
balloon_up = False
score = 0
bird_up = True
make_flap = 0

def draw():
    screen.blit('background',(0,0))
    if not game_over:
        balloon.draw()
        tree.draw()
        house.draw()
        bird.draw()
        screen.draw.text("Score: "+str(score),(10,10),fontsize=23)
    else:
        screen.draw.text("Score: "+str(score),center=(400,300),fontsize=50)
        
def on_mouse_down():
    global balloon_up
    balloon_up= True
    balloon.y = balloon.y-50

def on_mouse_up():
    global balloon_up
    balloon_up = False

def flap():
    global bird_up
    if bird_up:
        bird.image = "bird-down"
        bird_up= False
    else:
        bird.image = "bird-up"
        bird_up= True

def update():
    global score, game_over,make_flap
    if not game_over:
        if not balloon_up:
            balloon.y = balloon.y+1
        if house.right>0:
            house.x = house.x-2
        else:
            house.x=randint(800,1600)
            score = score + 1
        if tree.right>0:
            tree.x = tree.x -1
        else:
            tree.x = randint(800,1600)
            score = score + 1
        if bird.x>0:
            bird.x = bird.x-4
            if make_flap==9:
                flap()
                make_flap = 0
            else:
                make_flap = make_flap+1
        else:
            bird.pos=(randint(800,1600),randint(10,150))
            score = score + 1
            make_flap = 0
        if balloon.collidepoint(tree.x,tree.y) or balloon.collidepoint(house.x,house.y) or balloon.collidepoint(bird.x,bird.y):
            game_over = True
        if balloon.bottom > 560 or balloon.y<10:
            game_over = True
    
pgzrun.go()     
