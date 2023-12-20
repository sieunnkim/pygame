import random
import pgzrun
#Upper = not changing values
WIDTH=800 
HEIGHT=600
CENTER_X=400
CENTER_Y=300
CENTER=(400,300)
FINAL_LEVEL = 9
START_SPEED=10
COLORS=['green','blue']#random.choice (randomly bring the star out)
#lower = changing values
game_over = False #lost
game_complete = False #win
current_level = 1
stars=[]
animations=[]
score = 0
def draw():
    global stars, current_level, game_over, game_complete
    screen.clear()
    screen.blit('space',(0,0)) #background
    screen.draw.text("Score:"+str(score),fontsize =25,topleft =(10,10), color = "white")
    if game_over:
        display_message("GAME OVER", "try again")
    elif game_complete:
        display_message("YOU WON", "well done")
    else: #currently playing the game
        for star in stars:
            star.draw()
def update():
    global stars, current_level
    if len(stars)==0:
        stars = make_stars(current_level)

def make_stars(extra_stars):
    colors_to_create = get_colors_to_create(extra_stars)#choose color
    new_stars = create_stars(colors_to_create)#display star
    layout_stars(new_stars)#layout it
    animate_stars(new_stars)#make it move
    return new_stars
    
def get_colors_to_create(extra_stars):
    colors_to_create=['red']
    for i in range(0,extra_stars):
        random_color=random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create

def create_stars(colors_to_create): #list of colors are in the "colors_to_create"
    new_stars=[]
    for x in colors_to_create:
        star = Actor(x+'-star')
        new_stars.append(star)
    return new_stars #we append IMAGES in the list

def layout_stars(stars_to_layout): #new stars will come in for stars_to_layout
    num_of_gaps = len(stars_to_layout)+1
    gap_size = WIDTH/num_of_gaps
    random.shuffle(stars_to_layout)
    for index,star in enumerate(stars_to_layout):
        star.x=(index+1)*gap_size
def animate_stars(stars_to_animate):
    global animations
    for star in stars_to_animate:
        duration = START_SPEED - current_level
        star.anchor = ("center","bottom")
        animation = animate(star,duration=duration,on_finished=handle_gameover,y=HEIGHT)
        animations.append(animation)

def display_message(x,y):
    screen.draw.text(x,fontsize =60, center = CENTER, color = "white")
    screen.draw.text(y,fontsize =30, center =(CENTER_X,CENTER_Y+30), color = "white")

def handle_gameover():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global stars, currnet_level, score
    for x in stars:
        if x.collidepoint(pos):
            if "red" in x.image:
                red_star_click()
                score = score+1
            else:
                handle_gameover()

def red_star_click():
    global stars, current_level, animations, game_complete, FINAL_LEVEL
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level = current_level+1
        stars=[]
        animations=[]

def stop_animations(list_animation):
    for x in list_animation:
        if x.running:
            x.stop()


pgzrun.go()
