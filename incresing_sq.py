import pgzrun
import random

HEIGHT = 300
WIDTH = 300
def draw():
    screen.clear()
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    width = WIDTH
    height = HEIGHT -100
    for i in range(30000):
        box = Rect((0,0),(width,height))
        box.center = (150,150)
        screen.draw.rect(box,(r,g,b))
        width -=10
        height +=10
pgzrun.go()




    
