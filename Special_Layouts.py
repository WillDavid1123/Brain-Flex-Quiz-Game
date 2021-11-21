#Special layouts for Special questions

from graphics import *
import time

#Layout for Family Feud 
def FF(window, question, b1, b2, b3, b4, b5, b6, b7, op1, op2, op3, op4, correct, score):

    win = window
    ans = "p"

    #Create box and text for Question
    que = Rectangle(Point(97,92), Point(3,82))
    que.setFill(color_rgb(110, 139, 212))
    quetext = Text(Point(50, 87), question)
    quetext.setSize(30)

    #Create boxes for board and top answers (b#box = box, text = known answer, text2 = given score)
    
    b1box = Rectangle(Point(50,77), Point(3,71))
    b1box.setFill(color_rgb(110, 165, 212))
    b1text = Text(Point(20, 74), b1)
    b1text.setSize(28)
    b1text2 = Text(Point(45, 74), "54")
    b1text2.setSize(28)
    
    b2box = Rectangle(Point(50,71), Point(3,65))
    b2box.setFill(color_rgb(110, 165, 212))
    b2text = Text(Point(20, 68), b2)
    b2text.setSize(28)
    b2text2 = Text(Point(45, 68), "23")
    b2text2.setSize(28)
    
    b3box = Rectangle(Point(50,65), Point(3,59))
    b3box.setFill(color_rgb(110, 165, 212))
    b3text = Text(Point(20, 62), b3)
    b3text.setSize(28)
    b3text2 = Text(Point(45, 62), "9")
    b3text2.setSize(28)

    b4box = Rectangle(Point(50,59), Point(3,53))
    b4box.setFill(color_rgb(110, 165, 212))
    b4text = Text(Point(20, 56), b4)
    b4text.setSize(28)
    b4text2 = Text(Point(45, 56), "6")
    b4text2.setSize(28)

    b5box = Rectangle(Point(50,77), Point(97,71))
    b5box.setFill(color_rgb(110, 165, 212))
    b5text = Text(Point(70, 74), b5)
    b5text.setSize(28)
    b5text2 = Text(Point(95, 74), "4")
    b5text2.setSize(28)
    
    b6box = Rectangle(Point(50,71), Point(97,65))
    b6box.setFill(color_rgb(110, 165, 212))
    b6text = Text(Point(70, 68), b6)
    b6text.setSize(28)
    b6text2 = Text(Point(95, 68), "2")
    b6text2.setSize(28)
    
    b7box = Rectangle(Point(50,65), Point(97,59))
    b7box.setFill(color_rgb(110, 165, 212))
    b7text = Text(Point(70, 62), b7)
    b7text.setSize(28)
    b7text2 = Text(Point(95, 62), "1")
    b7text2.setSize(28)

    b8box = Rectangle(Point(50,59), Point(97,53))
    b8box.setFill(color_rgb(110, 165, 212))
    b8text = Text(Point(73.5, 56), "8")
    b8text.setSize(28)
    b8text.setTextColor("red")
    
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
    an3ind.setSize(20)
    an3text = Text(Point(26,12), op3)
    an3text.setSize(30)
    
    an4 = Rectangle(Point(97,2), Point(51,22))
    an4.setFill(color_rgb(126, 242, 124))
    an4ind = Text(Point(53,19), "R)")
    an4ind.setSize(20)
    an4text = Text(Point(76,12), op4)
    an4text.setSize(30)

    #Text so player knows how to leave the game
    leaving = Text(Point(13, 95), "Press L to leave")
    leaving.setSize(20)

    #Get a guess and see if it is right
    answer = 0

    while answer == 0:
        if ans == "y":
            break
        else: #Draw here so leaving and invalid answer works
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
            b1box.draw(win)
            b1text.draw(win)
            b1text2.draw(win)
            b2box.draw(win)
            b2text.draw(win)
            b2text2.draw(win)
            b3box.draw(win)
            b3text.draw(win)
            b3text2.draw(win)
            b4box.draw(win)
            b4text.draw(win)
            b4text2.draw(win)
            b5box.draw(win)
            b5text.draw(win)
            b5text2.draw(win)
            b6box.draw(win)
            b6text.draw(win)
            b6text2.draw(win)
            b7box.draw(win)
            b7text.draw(win)
            b7text2.draw(win)
            b8box.draw(win)
            b8text.draw(win)
            leaving.draw(win)
            guess = win.getKey()
            guess = guess.lower()
        
            if guess == correct: #Right answer
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

            elif guess != "q" and guess != "w" and guess != "e" and guess != "r" and guess != "l": #Invalid answer
                inv = Text(Point(50, 50), "Please pick an answer")
                inv.setSize(20)
                inv.setTextColor("blue")
                inv.draw(win)
                win.getMouse
                time.sleep(2)
                inv.undraw() #Undraw all so loop works
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
                wrong = Text(Point(50, 50), "Thats incorrect")
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
    leaving.undraw()

    return score


#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

# Layout for Jep.

def Jep(window, points, question, wist, op1, op2, op3, op4, correct, score):
    #Set up var
    win = window
    ans = "p"

    #Create box and text for Question
    que = Rectangle(Point(97,92), Point(3,65))
    que.setFill(color_rgb(110, 139, 212))
    if len(question) > 120: #Creates more lines if question is over 120 characters
        que1 = Text(Point(50, 83.5), question[:60])
        que2 = Text(Point(50, 78.5), question[60:120])
        que3 = Text(Point(50, 72.5), question[120:])
        que1.setSize(25)
        que2.setSize(25)
        que3.setSize(25)
        if question[40] != " ":
            que1 = Text(Point(50, 83.5), question[:60] + "-")
            que1.setSize(25)
        if question[80] != " ":
            que2 = Text(Point(50, 78.5), question[60:120] + "-")
            que2.setSize(25)

    elif len(question) > 60: ##Creates more lines if question is over 60 characters
        que1 = Text(Point(50, 80), question[:60])
        que2 = Text(Point(50, 75), question[60:])
        que1.setSize(25)
        que2.setSize(25)
        if question[40] != " ":
            que1 = Text(Point(50, 80), question[:60] + "-")
            que1.setSize(25)
    else:
        quetext = Text(Point(50, 78.5), question)
        quetext.setSize(30)

    #Create box and text for "Who is..."
    wis = Rectangle(Point(97,63), Point(3,48))
    wis.setFill(color_rgb(110, 139, 212))
    wistext = Text(Point(50, 55.5), wist)
    wistext.setSize(30)

    #Create text for possible score
    possscore = Text(Point(50, 95), ("Possible Points", points))
    possscore.setSize(20)

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
    an3ind.setSize(20)
    an3text = Text(Point(26,12), op3)
    an3text.setSize(30)
    
    an4 = Rectangle(Point(97,2), Point(51,22))
    an4.setFill(color_rgb(126, 242, 124))
    an4ind = Text(Point(53,19), "R)")
    an4ind.setSize(20)
    an4text = Text(Point(76,12), op4)
    an4text.setSize(30)

    #Text so player knows how to leave the game
    leaving = Text(Point(13, 95), "Press L to leave")
    leaving.setSize(20)

    #Get a guess and see if it is right and add glitches
    answer = 0

    while answer == 0:
        if ans == "y":
            break
        else: #Draw here so leaving and invalid answer works
            que.draw(win)
            if len(question) > 120:
                que1.draw(win)
                que2.draw(win)
                que3.draw(win)
            elif len(question) > 60:
                que1.draw(win)
                que2.draw(win)
            else:
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
            wis.draw(win)
            wistext.draw(win)
            possscore.draw(win)
            guess = win.getKey()
            guess = guess.lower()
        
            if guess == correct: #Right answer
                wis.undraw()
                wistext.undraw()
                cor = Text(Point(50, 55.5), "Thats correct")
                cor.setSize(20)
                cor.setTextColor("green")
                cor.draw(win)
                score = score + points
                score2.setText(score)
                win.getMouse
                time.sleep(2)
                cor.undraw()
                answer = 1

            elif guess != "q" and guess != "w" and guess != "e" and guess != "r" and guess != "l": #Invalid answer
                wis.undraw()
                wistext.undraw()
                inv = Text(Point(50, 55.5), "Please pick an answer")
                inv.setSize(20)
                inv.setTextColor("blue")
                inv.draw(win)
                win.getMouse
                time.sleep(2)
                inv.undraw() #Undraw all so loop works
                que.undraw()
                if len(question) > 120:
                    que1.undraw()
                    que2.undraw()
                    que3.undraw()
                elif len(question) > 60:
                    que1.undraw()
                    que2.undraw()
                else:
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
                possscore.undraw()
                leaving.undraw()
                answer = 0

            elif guess == "l": #Leaving screen setup
                que.undraw()
                if len(question) > 120:
                    que1.undraw()
                    que2.undraw()
                    que3.undraw()
                elif len(question) > 60:
                    que1.undraw()
                    que2.undraw()
                else:
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
                wis.undraw()
                wistext.undraw()
                possscore.undraw()
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
                wis.undraw()
                wistext.undraw()
                wrong = Text(Point(50, 55.5), "Thats incorrect")
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
    if len(question) > 120:
        que1.undraw()
        que2.undraw()
        que3.undraw()
    elif len(question) > 60:
        que1.undraw()
        que2.undraw()
    else:
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
    possscore.undraw()
    leaving.undraw()

    return score

#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

#Layout for are you smarter than a 5th grader

def s5thgrader(window, question, hint, op1, op2, op3, op4, correct, score):
    #Set up var
    win = window
    ans = "p"
    points = 100
    #Create box and text for Question
    que = Rectangle(Point(97,92), Point(3,60))
    que.setFill(color_rgb(110, 139, 212))
    quetext = Text(Point(50, 76), question)
    quetext.setSize(30)

    #Create box and text for the hint
    hintbox = Rectangle(Point(97,57), Point(3,47))
    hintbox.setFill(color_rgb(110, 139, 212))
    hinttext = Text(Point(50, 52), "Get (H)elp from a 5th grader")
    hinttext.setSize(25)

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
    an3ind.setSize(20)
    an3text = Text(Point(26,12), op3)
    an3text.setSize(30)
    
    an4 = Rectangle(Point(97,2), Point(51,22))
    an4.setFill(color_rgb(126, 242, 124))
    an4ind = Text(Point(53,19), "R)")
    an4ind.setSize(20)
    an4text = Text(Point(76,12), op4)
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
            hintbox.draw(win)
            hinttext.draw(win)
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
            guess = win.getKey()
            guess = guess.lower()
        
            if guess == correct: #Right answer
                hintbox.undraw()
                hinttext.undraw()
                cor = Text(Point(50, 53), "Thats correct")
                cor.setSize(20)
                cor.setTextColor("green")
                cor.draw(win)
                score = score + points
                score2.setText(score)
                win.getMouse
                time.sleep(2)
                cor.undraw()
                answer = 1

            elif guess == "h": #Get help for half the score
                que.undraw()
                quetext.undraw()
                hintbox.undraw()
                hinttext.undraw()
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
                clue = Text(Point(50,50), hint)
                clue.setSize(30)
                clue.draw(win)
                time.sleep(1)
                nxt = Text(Point(50, 5), "Click to Continue")
                nxt.setSize(15)
                nxt.draw(win)
                win.getMouse()
                points = 50
                clue.undraw()
                nxt.undraw()
                

            elif guess != "q" and guess != "w" and guess != "e" and guess != "r" and guess != "l": #Invalid answer
                hintbox.undraw()
                hinttext.undraw()
                inv = Text(Point(50, 53), "Please pick an answer")
                inv.setSize(20)
                inv.setTextColor("blue")
                inv.draw(win)
                win.getMouse
                time.sleep(2)
                inv.undraw() #Undraw so loop works
                que.undraw()
                quetext.undraw()
                hintbox.undraw()
                hinttext.undraw()
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
                hintbox.undraw()
                hinttext.undraw()
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
                hintbox.undraw()
                hinttext.undraw()
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
    hintbox.undraw()
    hinttext.undraw()
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
    score = FF(win, "What is your favorite room?", "Bathroom", "Livingroom", "Dinningroom", "Bedroom", "Ballroom", "Dressingroom", "Storageroom", "Weightroom", "Dungeon", "Courtyard", "Outside", "q", score)
    score = Jep(win, 100, "He invented the light bulb and 100+ other inventions", "Who is...", "Einstein", "Tesla", "Batman", "Elon Musk", "q", score)
    score = Jep(win, 100, "This is a test to see if the 60+ character line seperator works ok lalalalalalalalalalalalalalala", "Who is...", "Einstein", "Tesla", "Batman", "Elon Musk", "q", score)
    score = Jep(win, 100, "This is a test to see if the 120+ character line seperator works ok lalalalalalalalalalalalalalala wow 120+ is really long lalalalalalalalalalalalalalalalala", "Who is...", "Einstein", "Tesla", "Batman", "Elon Musk", "q", score)
    score = s5thgrader(win, "How many feet are in a mile?", "5 tomatos", "4036", "2080", "5280", "3089", "e", score)
if __name__ == "__main__":
    main() 
