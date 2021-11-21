#Text for hosts
from graphics import *
import time

#Text
def host(window, h, score, text):

    win = window

    #Text for the Hosts (Color based on host)
    if len(text) > 44: #44 characters or above
        ht1 = Text(Point(50, 55), text[:45])
        ht2 = Text(Point(50, 45), text[45:])
        ht1.setSize(30)
        ht2.setSize(30)
        if text[44] != " ":
            ht1 = Text(Point(50, 55), text[:44] + "-")
            ht2 = Text(Point(50, 45), text[44:])
            ht1.setSize(30)
            ht2.setSize(30)
        if h == 1: #Brain Game
            ht1.setTextColor("dark blue")
            ht2.setTextColor("dark blue")
        if h == 2: #Family Feud
            ht1.setTextColor("red")
            ht2.setTextColor("red")
        if h == 3: #Jepordy
            ht1.setTextColor("purple")
            ht2.setTextColor("purple")
        if h == 4: #Are you smarter than a 5th grader
            ht1.setTextColor("green")
            ht2.setTextColor("green")
        if h == 5: #White Brain Game Text
            ht1.setTextColor("white")
            ht2.setTextColor("white")
        ht1.draw(win)
        ht2.draw(win)

    else:
        ht = Text(Point(50, 50), text)
        ht.setSize(30)
        if h == 1: #Brain Game
            ht.setTextColor("dark blue")
        if h == 2: #Family Feud
            ht.setTextColor("red")
        if h == 3: #Jepordy
            ht.setTextColor("purple")
        if h == 4: #Are you smarter than a 5th grader
            ht.setTextColor("green")
        if h == 5: #White Brain Game Text
            ht.setTextColor("white")
        ht.draw(win)
    time.sleep(1)
    nxt = Text(Point(50, 5), "Click to Continue")
    if h == 5: #White Brain Game Text
        nxt.setTextColor("white")
    nxt.setSize(15)
    nxt.draw(win)
    win.getMouse()
    nxt.undraw()
    if len(text) > 44:
        ht1.undraw()
        ht2.undraw()
    else:
        ht.undraw()

    return score
    
def main():
    w = 1000
    h = 650
    win = GraphWin("Brain Flex the game", w , h)
    win.setCoords(0.0 ,0.0 ,100.0, 100.0)
    win.setBackground("light blue")
    score = 0
    h = 1
    host(win, h, score, "Welcome Everyone")
    h = 2
    host(win, h, score, "123456789123456789123456789123456789123456789123456789")
    h = 3
    host(win, h, score, "Jepordy!!!!!!!!!")
    h = 4
    host(win, h, score, "And his name is John Cena!")
    h = 5
    host(win, h, score, "White Text!")
    h = 9
    host(win, h, score, "Black text!")
        
if __name__ == "__main__":
    main()
