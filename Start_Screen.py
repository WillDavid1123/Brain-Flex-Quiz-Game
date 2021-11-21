#Start screen to start the game or exit the program

from graphics import *

def Starting(window, score, plays):

    win = window
    #Create box and text for Title
    title = Rectangle(Point(85,97), Point(15,75))
    title.setFill(color_rgb(110, 139, 212))
    title.draw(win)
    titletext1 = Text(Point(50, 91), "WELCOME TO")
    titletext1.setSize(35)
    titletext1.draw(win)
    titletext2 = Text(Point(50, 79), "BRAIN FLEXING THE GAME")
    titletext2.setSize(35)
    titletext2.draw(win)

    #Create boxes and text for options
    stabox = Rectangle(Point(95,50), Point(5,65))
    stabox.setFill(color_rgb(110, 139, 212))
    stabox.draw(win)
    statext = Text(Point(50, 57.5), "(S)TART THE GAME")
    statext.setSize(35)
    statext.draw(win)

    helpbox = Rectangle(Point(95,30), Point(5,45))
    helpbox.setFill(color_rgb(110, 139, 212))
    helpbox.draw(win)
    helptext = Text(Point(50, 37.5), "(H)elp (Recommended for first play)")
    helptext.setSize(35)
    helptext.draw(win)

    exitbox = Rectangle(Point(95,10), Point(5,25))
    exitbox.setFill(color_rgb(110, 139, 212))
    exitbox.draw(win)
    exittext = Text(Point(50, 17.5), "(E)XIT (NOT RECOMMENDED)")
    exittext.setSize(35)
    exittext.draw(win)

    if score != 0 or plays != 0: #Show previous score if game has already been played
        prescore = Text(Point(50, 72), ("Previous Score: ", score))
        prescore.setSize(20)
        prescore.draw(win)

    while True:
        #Get choice from user
        choice = win.getKey()
        choice = choice.lower()

        #Start the game
        if choice == "s":
            title.undraw()
            titletext1.undraw()
            titletext2.undraw()
            stabox.undraw()
            statext.undraw()
            helpbox.undraw()
            helptext.undraw()
            exitbox.undraw()
            exittext.undraw()
            if score != 0 or plays != 0:
                prescore.undraw()
            break
        
        #Open Help for text colors and basic instructions
        elif choice == "h":
            title.undraw()
            titletext1.undraw()
            titletext2.undraw()
            stabox.undraw()
            statext.undraw()
            helpbox.undraw()
            helptext.undraw()
            exitbox.undraw()
            exittext.undraw()
            if score != 0 or plays != 0:
                prescore.undraw()

            title = Text(Point(50, 95), "Brain Flex Basics")
            title.setSize(35)
            title.setStyle("bold")
            title.setFace("courier")
            title.draw(win)
            black = Text(Point(50, 80), "Black text     -     Programmer/Other Voice")
            black.setSize(30)
            black.draw(win)
            blue = Text(Point(50, 70), "Dark Blue text     -     Brain Flex Host")
            blue.setTextColor("dark blue")
            blue.setSize(30)
            blue.draw(win)
            red = Text(Point(50, 60), "Red text     -     Family Feud")
            red.setTextColor("red")
            red.setSize(30)
            red.draw(win)
            purple = Text(Point(50, 50), "Purple text     -     Jepordy")
            purple.setTextColor("purple")
            purple.setSize(30)
            purple.draw(win)
            green = Text(Point(50, 40), "Green text     -     Are You Smarter Than a 5th Grader")
            green.setTextColor("green")
            green.setSize(30)
            green.draw(win)
            btt = Text(Point(50, 3), "CLICK TO GO BACK TO TITLE SCREEN")
            btt.setSize(15)
            btt.draw(win)
            win.getMouse()
            title.undraw()
            black.undraw()
            blue.undraw()
            red.undraw()
            purple.undraw()
            green.undraw()
            btt.undraw()
            Starting(win, score, plays)

        #Exit game
        elif choice == "e":
            title.undraw()
            titletext1.undraw()
            titletext2.undraw()
            stabox.undraw()
            statext.undraw()
            helpbox.undraw()
            helptext.undraw()
            exitbox.undraw()
            exittext.undraw()
            if score != 0 or plays != 0:
                prescore.undraw()
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
                win.close()
            else:
                lea.undraw()
                ylea.undraw()
                nlea.undraw()
                Starting(win, score, plays)

        else:
            title.undraw()
            titletext1.undraw()
            titletext2.undraw()
            stabox.undraw()
            statext.undraw()
            helpbox.undraw()
            helptext.undraw()
            exitbox.undraw()
            exittext.undraw()
            Starting(win, score, plays)

        break

def main():
    w = 1000
    h = 650
    win = GraphWin("Brain Flex the game", w , h)
    win.setCoords(0.0 ,0.0 ,100.0, 100.0)
    win.setBackground("light blue")
    score = 0
    plays = 0
    Starting(win, score, plays)

if __name__ == "__main__":
    main()

