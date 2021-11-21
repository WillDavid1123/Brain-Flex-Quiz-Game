# Layout of the question and answers

from graphics import *
import time
import random

def layout(window, g, question, op1, op2, op3, op4, correct, score):
    #Set up var
    win = window
    ans = "p"
    qglitch = ""
    #Create box and text for Question
    que = Rectangle(Point(97,92), Point(3,60))
    que.setFill(color_rgb(110, 139, 212))
    quetext = Text(Point(50, 76), question)
    if g >= 5: #Changes font and color when glitch level is high enough
        font = random.random()*100
        if font <= 25:
            quetext.setFace("helvetica")
        elif font >= 25 and font <= 50:
            quetext.setFace("courier")
        elif font >= 50 and font <= 75:
            quetext.setFace("times roman")
        else:
            quetext.setFace("arial")
        quetext.setTextColor(color_rgb(random.randint(0,250),random.randint(0,250),random.randint(0,250)))
    quetext.setSize(30) 

    #Create a scoreboard
    score1 = Text(Point(90, 95), "Score: ")
    score1.setSize(20)
    score2 = Text(Point(96.5, 95), score)
    score2.setSize(20)

    #Create boxes and text for answers (an# = box, ind = indicator, text = possible answer)
    an1 = Rectangle(Point(49,25), Point(3,45))
    an1.setFill(color_rgb(126, 242, 124))
    an1ind = Text(Point(5,42), "Q)")
    an1ind.setSize(20)
    an1text = Text(Point(26,35), op1)
    if g >= 5: #Changes font and color when glitch level is high enough
        font = random.random()*100
        if font <= 25:
            an1text.setFace("helvetica")
        elif font >= 25 and font <= 50:
            an1text.setFace("courier")
        elif font >= 50 and font <= 75:
            an1text.setFace("times roman")
        else:
            an1text.setFace("arial")
        an1text.setTextColor(color_rgb(random.randint(0,250),random.randint(0,250),random.randint(0,250)))
    an1text.setSize(30)
    
    an2 = Rectangle(Point(97,25), Point(51,45))
    an2.setFill(color_rgb(126, 242, 124))
    an2ind = Text(Point(53,42), "W)")
    an2ind.setSize(20)
    an2text = Text(Point(76,35), op2)
    an2text.setSize(30)
    
    an3 = Rectangle(Point(49,2), Point(3,22))
    an3.setFill(color_rgb(126, 242, 124))
    an3ind = Text(Point(5,19), "E)")
    if g >= 5: #Changes font and color when glitch level is high enough
        font = random.random()*100
        if font <= 25:
            an3ind.setFace("helvetica")
        elif font >= 25 and font <= 50:
            an3ind.setFace("courier")
        elif font >= 50 and font <= 75:
            an3ind.setFace("times roman")
        else:
            an3ind.setFace("arial")
        an3ind.setTextColor(color_rgb(random.randint(0,250),random.randint(0,250),random.randint(0,250)))
    an3ind.setSize(20)
    an3text = Text(Point(26,12), op3)
    an3text.setSize(30)
    
    an4 = Rectangle(Point(97,2), Point(51,22))
    an4.setFill(color_rgb(126, 242, 124))
    an4ind = Text(Point(53,19), "R)")
    an4ind.setSize(20)
    an4text = Text(Point(76,12), op4)
    if g >= 5: #Changes font and color when glitch level is high enough
        font = random.random()*100
        if font <= 25:
            an4text.setFace("helvetica")
        elif font >= 25 and font <= 50:
            an4text.setFace("courier")
        elif font >= 50 and font <= 75:
            an4text.setFace("times roman")
        else:
            an4text.setFace("arial")
        an4text.setTextColor(color_rgb(random.randint(0,250),random.randint(0,250),random.randint(0,250)))
    an4text.setSize(30)

    #Text so player knows how to leave the game
    leaving = Text(Point(13, 95), "Press L to leave")
    leaving.setSize(20)

    #Get a guess and see if it is right and add glitches
    answer = 0

    while answer == 0:
        if ans == "y":
            break
        else: #Draw here so invalid and leaving works
            que.draw(win)
            quetext.draw(win)
            an1.draw(win)
            an1ind.draw(win)
            an1text.draw(win)
            an2.draw(win)
            an2ind.draw(win)
            an2text.draw(win)
            an3.draw(win)
            an3ind.draw(win)
            an3text.draw(win)
            an4.draw(win)
            an4ind.draw(win)
            an4text.draw(win)
            score1.draw(win)
            score2.draw(win)
            leaving.draw(win)
            if g >= 1:
                for gli in range(g):
                    y1 = random.random() * 100
                    y2 = y1 + (random.random()*5)
                    x1 = random.random() * 100
                    x2 = x1 + (random.random()*5)
                    glitch = Rectangle(Point(x1, y1), Point(x2, y2))
                    glitch.draw(win)
                    glitch.setFill(color_rgb(255, 0, 255))
                    time.sleep(.1)
                    glitch.setFill(color_rgb(0, 0, 0))
                    time.sleep(.1)
                    glitch.undraw()
            guess = win.getKey()
            guess = guess.lower()
        
            if guess == correct: #Right answer
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

            elif guess != "q" and guess != "w" and guess != "e" and guess != "r" and guess != "l": #Invalid answer
                inv = Text(Point(50, 53), "Please pick an answer")
                inv.setSize(20)
                inv.setTextColor("blue")
                inv.draw(win)
                win.getMouse
                time.sleep(2)
                inv.undraw() #Undraw so loop works
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
                leaving.undraw()
                answer = 0

            elif guess == "l": #Leaving screen setup
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
                leaving.undraw()
                lea = Text(Point(50, 50), "Are you sure you want to Leave?")
                lea.setSize(30)
                ylea = Text(Point(30, 40), "(Y)es")
                ylea.setSize(20)
                nlea = Text(Point(70, 40), "No (Any other key)")
                nlea.setSize(20)
                lea.draw(win)
                ylea.draw(win)
                nlea.draw(win)
                ans = win.getKey()

                if ans.lower() == "y":
                    lea.undraw()
                    ylea.undraw()
                    nlea.undraw()
                    end = Text(Point(50, 50), "Thanks for playing!")
                    end.setSize(30)
                    end.draw(win)
                    time.sleep(1)
                    nxt = Text(Point(50, 5), "Click to Continue")
                    nxt.setSize(15)
                    nxt.draw(win)
                    win.getMouse()
                    end.undraw()
                    nxt.undraw()
                    escore = Text(Point(50, 50), ("Your score was: ", score))
                    escore.setSize(30)
                    escore.draw(win)
                    time.sleep(1)
                    nxt = Text(Point(50, 5), "Click to Leave Game")
                    nxt.setSize(15)
                    nxt.draw(win)
                    win.getMouse()
                    escore.undraw()
                    nxt.undraw()
                    win.close()

                else:
                    lea.undraw()
                    ylea.undraw()
                    nlea.undraw()
                    exit



            else: #Wrong answer
                wrong = Text(Point(50, 53), "Thats incorrect")
                wrong.setSize(20)
                wrong.setTextColor("red")
                wrong.draw(win)
                win.getMouse
                time.sleep(2)
                wrong.undraw()
                answer = 1

            if ans.lower() == "y":
                exit

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
    leaving.undraw()

    return score

def main():
    w = 1000
    h = 650
    win = GraphWin("Brain Flex the game", w , h)
    win.setCoords(0.0 ,0.0 ,100.0, 100.0)
    win.setBackground("light blue")
    score = 0
    g = 0
    #score = layout(win, g, "What is the square root of 81?", "3", "7", "9", "What's a square root?", "e", 0)
    g = 1
    score = layout(win, g, "What is the capital of Michigan?", "Detroit", "Kalamazoo", "Hell", "Lansing", "r", score)
    g = 3
    score = layout(win, g, "What is 106 times 6?", "636", "730", "630", "102", "q", score)
    g = 5
    score = layout(win, g, "What is the square root of 81?", "3", "7", "9", "What's a square root?", "e", score)
    
if __name__ == "__main__":
    main()
