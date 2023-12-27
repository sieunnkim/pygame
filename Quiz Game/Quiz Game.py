import pgzrun
WIDTH = 1280
HEIGHT = 720
#size of boxes
qbox = Rect(0,0,820,240)
tbox = Rect(0,0,240,240)
abox1 = Rect(0,0,495,165)
abox2 = Rect(0,0,495,165)
abox3 = Rect(0,0,495,165)
abox4 = Rect(0,0,495,165)
#location of boxes
qbox.move_ip(50,40)
tbox.move_ip(990,40)
abox1.move_ip(50,358)
abox2.move_ip(735,358)
abox3.move_ip(50,538)
abox4.move_ip(735,538)

q1 =["10+10","10","20","30","40",2]
q2 =["10+20","30","50","10","60",1]
q3 =["10+30","5","80","50","40",4]
q4 =["10+40","50","20","30","40",1]
q5 =["20+20","60","20","40","50",3]

aboxes = [abox1,abox2,abox3,abox4]
questions=[q1,q2,q3,q4,q5] #questions contains list
score=0
time_left=10
thisq=questions.pop(0)

def draw():
    screen.fill("white")
    screen.draw.filled_rect(qbox,"gray")
    screen.draw.filled_rect(tbox,"sky blue")
    x=1
    for box in aboxes:
        screen.draw.filled_rect(box,"blue")
        screen.draw.textbox(thisq[x],box)
        x=x+1
    screen.draw.textbox(str(time_left),tbox)
    screen.draw.textbox(thisq[0],qbox)
def gameover():
    global thisq,time_left,score
    message = "Game Over. You got %s questions correct"%str(score)
    thisq=[message,'-','-','-','-',5]
    time_left=0
def correct_ans():
    global thisq,time_left,score
    score=score+1
    if questions:
        thisq=questions.pop(0)
        time_left=10
    else:
        gameover()
def on_mouse_down(pos):
    x=1
    for box in aboxes:
        if box.collidepoint(pos):
            if x==thisq[5]:
                correct_ans()
            else:
                gameover()
        x=x+1
def t_reduce():
    global time_left
    if time_left:
        time_left=time_left-1
    else:
        gameover()
clock.schedule_interval(t_reduce,1.0)

pgzrun.go()
