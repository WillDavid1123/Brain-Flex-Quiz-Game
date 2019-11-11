# Layout of the question and answers

from graphics import *
import time
import random

def layout(window, g, question, op1, op2, op3, op4, correct, score):

    win = window

    #Create box and text for Question
    que = Rectangle(Point(97,92), Point(3,60))
    que.setFill(color_rgb(110, 139, 212))
    que.draw(win)
    quetext = Text(Point(50, 76), question)
    quetext.setSize(30)
    quetext.draw(win)

    #Create a scoreboard
    score1 = Text(Point(90, 95), "Score: ")
    score1.setSize(20)
    score1.draw(win)
    score2 = Text(Point(96.5, 95), score)
    score2.setSize(20)
    score2.draw(win)

    #Create boxes and text for answers (an# = box, ind = indicator, text = possible answer)
    an1 = Rectangle(Point(49,25), Point(3,45))
    an1.setFill(color_rgb(126, 242, 124))
    an1.draw(win)
    an1ind = Text(Point(5,42), "Q)")
    an1ind.setSize(20)
    an1ind.draw(win)
    an1text = Text(Point(26,35), op1)
    an1text.setSize(30)
    an1text.draw(win)
    
    an2 = Rectangle(Point(97,25), Point(51,45))
    an2.setFill(color_rgb(126, 242, 124))
    an2.draw(win)
    an2ind = Text(Point(53,42), "W)")
    an2ind.setSize(20)
    an2ind.draw(win)
    an2text = Text(Point(76,35), op2)
    an2text.setSize(30)
    an2text.draw(win)
    
    an3 = Rectangle(Point(49,2), Point(3,22))
    an3.setFill(color_rgb(126, 242, 124))
    an3.draw(win)
    an3ind = Text(Point(5,19), "E)")
    an3ind.setSize(20)
    an3ind.draw(win)
    an3text = Text(Point(26,12), op3)
    an3text.setSize(30)
    an3text.draw(win)
    
    an4 = Rectangle(Point(97,2), Point(51,22))
    an4.setFill(color_rgb(126, 242, 124))
    an4.draw(win)
    an4ind = Text(Point(53,19), "R)")
    an4ind.setSize(20)
    an4ind.draw(win)
    an4text = Text(Point(76,12), op4)
    an4text.setSize(30)
    an4text.draw(win)

    #Get a guess and see if it is right
    answer = 0

    if g == 1:
        y1 = random.random() * 100
        y2 = y1 + 3
        x1 = random.random() * 100
        x2 = x1 + 3
        glitch = Rectangle(Point(x1, y1), Point(x2, y2))
        glitch.draw(win)
        glitch.setFill(color_rgb(255, 0, 255))
        time.sleep(1)
        glitch.setFill(color_rgb(0, 0, 0))
        time.sleep(1)

    while answer == 0:
        guess = win.getKey()
        guess = guess.lower()
        
        if guess == correct:
            cor = Text(Point(50, 53), "Thats correct")
            cor.setSize(20)
            cor.setTextColor("green")
            cor.draw(win)
            score = score + 100
            score2.setText(score)
            win.getMouse
            time.sleep(2)
            cor.undraw()
            answer = 1

        elif guess != "q" and guess != "w" and guess != "e" and guess != "r":
            inv = Text(Point(50, 53), "Please pick an answer")
            inv.setSize(20)
            inv.setTextColor("blue")
            inv.draw(win)
            win.getMouse
            time.sleep(2)
            inv.undraw()
            answer = 0

        else:
            wrong = Text(Point(50, 53), "Thats incorrect")
            wrong.setSize(20)
            wrong.setTextColor("red")
            wrong.draw(win)
            win.getMouse
            time.sleep(2)
            wrong.undraw()
            answer = 1

    #Undraw everything to prepare for next section/question
    que.undraw()
    quetext.undraw()
    an1.undraw()
    an1ind.undraw()
    an1text.undraw()
    an2.undraw()
    an2ind.undraw()
    an2text.undraw()
    an3.undraw()
    an3ind.undraw()
    an3text.undraw()
    an4.undraw()
    an4ind.undraw()
    an4text.undraw()
    score1.undraw()
    score2.undraw()
    if g == 1:
        glitch.undraw()

    return score

def main():
    w = 1000
    h = 650
    win = GraphWin("Brain Flex the game", w , h)
    win.setCoords(0.0 ,0.0 ,100.0, 100.0)
    win.setBackground("light blue")
    g = 0
    score = layout(win, g, "What is the square root of 81?", "3", "7", "9", "What's a square root?", "e", 0)
    g = 1
    score = layout(win, g, "What is the capital of Michigan?", "Detroit", "Kalamazoo", "Hell", "Lansing", "r", score)
    score = layout(win, g, "What is 106 times 6?", "636", "730", "630", "102", "q", score)
    score = layout(win, g, "What is the square root of 81?", "3", "7", "9", "What's a square root?", "e", 0)
    
if __name__ == "__main__":
    main()
