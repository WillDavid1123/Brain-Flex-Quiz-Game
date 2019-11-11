#Special layouts for Special questions

from graphics import *
import time

def FF(window, question, b1, b2, b3, b4, b5, b6, b7, op1, op2, op3, op4, correct, score):

    win = window

    #Create box and text for Question
    que = Rectangle(Point(97,92), Point(3,82))
    que.setFill(color_rgb(110, 139, 212))
    que.draw(win)
    quetext = Text(Point(50, 87), question)
    quetext.setSize(30)
    quetext.draw(win)

    #Create boxes for board and top answers (b#box = box, text = known answer, text2 = given score)
    
    b1box = Rectangle(Point(50,77), Point(3,71))
    b1box.setFill(color_rgb(110, 165, 212))
    b1box.draw(win)
    b1text = Text(Point(20, 74), b1)
    b1text.setSize(28)
    b1text.draw(win)
    b1text2 = Text(Point(45, 74), "54")
    b1text2.setSize(28)
    b1text2.draw(win)
    
    b2box = Rectangle(Point(50,71), Point(3,65))
    b2box.setFill(color_rgb(110, 165, 212))
    b2box.draw(win)
    b2text = Text(Point(20, 68), b2)
    b2text.setSize(28)
    b2text.draw(win)
    b2text2 = Text(Point(45, 68), "23")
    b2text2.setSize(28)
    b2text2.draw(win)
    
    b3box = Rectangle(Point(50,65), Point(3,59))
    b3box.setFill(color_rgb(110, 165, 212))
    b3box.draw(win)
    b3text = Text(Point(20, 62), b3)
    b3text.setSize(28)
    b3text.draw(win)
    b3text2 = Text(Point(45, 62), "9")
    b3text2.setSize(28)
    b3text2.draw(win)

    b4box = Rectangle(Point(50,59), Point(3,53))
    b4box.setFill(color_rgb(110, 165, 212))
    b4box.draw(win)
    b4text = Text(Point(20, 56), b4)
    b4text.setSize(28)
    b4text.draw(win)
    b4text2 = Text(Point(45, 56), "6")
    b4text2.setSize(28)
    b4text2.draw(win)

    b5box = Rectangle(Point(50,77), Point(97,71))
    b5box.setFill(color_rgb(110, 165, 212))
    b5box.draw(win)
    b5text = Text(Point(70, 74), b5)
    b5text.setSize(28)
    b5text.draw(win)
    b5text2 = Text(Point(95, 74), "4")
    b5text2.setSize(28)
    b5text2.draw(win)
    
    b6box = Rectangle(Point(50,71), Point(97,65))
    b6box.setFill(color_rgb(110, 165, 212))
    b6box.draw(win)
    b6text = Text(Point(70, 68), b6)
    b6text.setSize(28)
    b6text.draw(win)
    b6text2 = Text(Point(95, 68), "2")
    b6text2.setSize(28)
    b6text2.draw(win)
    
    b7box = Rectangle(Point(50,65), Point(97,59))
    b7box.setFill(color_rgb(110, 165, 212))
    b7box.draw(win)
    b7text = Text(Point(70, 62), b7)
    b7text.setSize(28)
    b7text.draw(win)
    b7text2 = Text(Point(95, 62), "1")
    b7text2.setSize(28)
    b7text2.draw(win)

    b8box = Rectangle(Point(50,59), Point(97,53))
    b8box.setFill(color_rgb(110, 165, 212))
    b8box.draw(win)
    b8text = Text(Point(73.5, 56), "8")
    b8text.setSize(28)
    b8text.setTextColor("red")
    b8text.draw(win)
    
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

    while answer == 0:
        guess = win.getKey()
        guess = guess.lower()
        
        if guess == correct:
            cor = Text(Point(50, 50), "Thats correct")
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
            inv = Text(Point(50, 50), "Please pick an answer")
            inv.setSize(20)
            inv.setTextColor("blue")
            inv.draw(win)
            win.getMouse
            time.sleep(2)
            inv.undraw()
            answer = 0

        else:
            wrong = Text(Point(50, 50), "Thats incorrect")
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
    b1box.undraw()
    b1text.undraw()
    b1text2.undraw()
    b2box.undraw()
    b2text.undraw()
    b2text2.undraw()
    b3box.undraw()
    b3text.undraw()
    b3text2.undraw()
    b4box.undraw()
    b4text.undraw()
    b4text2.undraw()
    b5box.undraw()
    b5text.undraw()
    b5text2.undraw()
    b6box.undraw()
    b6text.undraw()
    b6text2.undraw()
    b7box.undraw()
    b7text.undraw()
    b7text2.undraw()
    b8box.undraw()
    b8text.undraw()

    return score

def main():
    w = 1000
    h = 650
    win = GraphWin("Brain Flex the game", w , h)
    win.setCoords(0.0 ,0.0 ,100.0, 100.0)
    win.setBackground("light blue")
    score = FF(win, "What is your favorite room?", "Bathroom", "Livingroom", "Dinningroom", "Bedroom", "Ballroom", "Dressingroom", "Storageroom", "Weightroom", "Dungeon", "Courtyard", "Outside", "q", 0)

if __name__ == "__main__":
    main() 
