import pgzrun
from random import randint

WIDTH=400
HEIGHT=400

dots = []
lines = []
timer = 0
time_limit= 30
next_dot = 0
game_over=False

for dot in range(0,10):
    actor = Actor("dot")
    actor.pos= randint(20,WIDTH-20),randint(20,HEIGHT-20)
    dots.append(actor)

def draw():
    screen.clear()
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text((str(number)),(dot.pos[0],dot.pos[1]+12))
        dot.draw()
        number = number+1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))
    if next_dot==10:
        screen.draw.text("WIN", center=(200,130),color="Blue",fontsize=100)
        screen.draw.text(str(round(timer,3)),center=(200,230),color="Blue", fontsize=50)
        game_over = True
    else:
        screen.draw.text(str(round(timer,3)), topleft=(10,10), color="red", fontsize = 20)
        if timer>= time_limit:
            screen.fill("Black")
            screen.draw.text("GAMEOVER", center=(200,200), color="red", fontsize=100)
            game_over=True

def update():
    global timer
    if next_dot!=10:
        timer = timer+(1/60)
def on_mouse_down(pos):
    global next_dot
    global lines
    if next_dot<10:
        if dots[next_dot].collidepoint(pos):
            if next_dot:
                lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
                sounds.click.play()
            next_dot = next_dot + 1
        else:
            lines = []
            next_dot = 0

pgzrun.go()
