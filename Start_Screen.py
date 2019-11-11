#Start screen to start the game or exit the program

from graphics import *

def Starting(window):

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

    optbox = Rectangle(Point(95,30), Point(5,45))
    optbox.setFill(color_rgb(110, 139, 212))
    optbox.draw(win)
    opttext = Text(Point(50, 37.5), "(O)TIONS (CHANGE STUFF!!)")
    opttext.setSize(35)
    opttext.draw(win)

    exitbox = Rectangle(Point(95,10), Point(5,25))
    exitbox.setFill(color_rgb(110, 139, 212))
    exitbox.draw(win)
    exittext = Text(Point(50, 17.5), "(E)XIT (NOT RECOMMENDED)")
    exittext.setSize(35)
    exittext.draw(win)

    #Get choice from user
    choice = win.getKey()

    #Start the game
    if choice == "s":
        title.undraw()
        titletext1.undraw()
        titletext2.undraw()
        stabox.undraw()
        statext.undraw()
        optbox.undraw()
        opttext.undraw()
        exitbox.undraw()
        exittext.undraw()
        win.close

    #Open Options
    elif choice == "o":
        title.undraw()
        titletext1.undraw()
        titletext2.undraw()
        stabox.undraw()
        statext.undraw()
        optbox.undraw()
        opttext.undraw()
        exitbox.undraw()
        exittext.undraw()

        comingsoon = Text(Point(50, 55), "COMING LATER IN DEVELOPMENT")
        comingsoon.setSize(35)
        comingsoon.draw(win)
        btt = Text(Point(50, 45), "CLICK TO GO BACK TO TITLE SCREEN")
        btt.setSize(35)
        btt.draw(win)
        win.getMouse()
        comingsoon.undraw()
        btt.undraw()
        Starting(win)

    #Exit game
    elif choice == "e":
        exit()
        

def main():
    w = 1000
    h = 650
    win = GraphWin("Brain Flex the game", w , h)
    win.setCoords(0.0 ,0.0 ,100.0, 100.0)
    win.setBackground("light blue")
    Starting(win)

if __name__ == "__main__":
    main()
