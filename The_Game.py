from graphics import *
import time
import random
from Question_Layout import layout
import Start_Screen 
from Special_Layouts import *
from Host_Text import host

def main():
    w = 1000
    h = 650
    win = GraphWin("Brain Flex the game", w , h)
    win.setCoords(0.0 ,0.0 ,100.0, 100.0)
    win.setBackground("light blue")
    score = 0
    plays = 0
    g = 0
    h = 1
    while True:
        Start_Screen.Starting(win, score, plays)
        if win.isClosed():
            break
        else:
            host(win, h, score, "Hello everyone")
            host(win, h, score, "My name is Y.A.S.H or")
            host(win, h, score, "Your Automated Show Host")
            host(win, h, score, "Today you are going to be testing a brand new kind of game show")
            host(win, h, score, "Something completely human-free")
            host(win, h, score, "Built entirely off of classics and favorites")
            host(win, h, score, "That being said, Welcome to")
            host(win, h, score, "Brain Flex!!")
            host(win, h, score, "A game show where you test your mental power against our randomly chosen question 'Challengers'")
            h = 9
            host(win, h, score, "(Currently in Beta, any and all bugs should be reported)")
            h = 1
            host(win, h, score, "Let's Begin!")
            score = layout(win, g, "What is the square root of 81?", "3", "7", "9", "What's a square root?", "e", 0)
            score = layout(win, g, "What's the shortcut for copy?", "ctrl v", "ctrl alt delete", "ctrl c", "c o p y", "e", score)
            score = layout(win, g, "What is meteorology the study of?", "Shooting Stars", "The Weather", "Meteors", "Stars", "w", score)
            score = layout(win, g, "Which car brand was the first to offer seat belts?", "Nash Motors", "Ford Motor Company", "General Motors", "Volkswagen", "q", score)
            score = layout(win, g, "Which organ has four chambers?", "Liver", "Kidney", "Lungs", "Heart", "r", score)
            g = 1
            score = layout(win, g, "What is the smallest country in the world?", "Malta", "Vatican City", "New Zealand", "Portugal", "w", score)
            score = layout(win, g, "Who lives in a pineapple under the sea?", "Jimmy Neutron", "Timmy Turner", "Spongebob Squarepants", "Johnny Test", "e", score)
            score = layout(win, g, "What is the capital of Michigan?", "Detroit", "Kalamazoo", "Hell", "Lansing", "r", score)
            score = layout(win, g, "How many hearts does an octopus have?", "0", "1", "3", "5", "e", score)
            g = 3
            score = layout(win, g, "What is a group of frogs called?", "A Pod", "An Army", "A Murder", "An Elope", "w", score)
            g = 5
            score = layout(win, g, "What is 106 times 6?", "636", "730", "630", "102", "q", score)
            g = 0
            host(win, h, score, "Wait, Wait, Wait, Hold up, Cut!")
            host(win, h, score, "What's going on here?")
            host(win, h, score, "Why are there all these gli-")
            win.setBackground("black")
            time.sleep(5)
            h = 5
            host(win, h, score, "Hello?")
            host(win, h, score, "Are you still there?")
            host(win, h, score, "I'm gonna try getting the lights back on just wait there")
            time.sleep(3)
            win.setBackground("light blue")
            h = 1
            host(win, h, score, "That's better, now-")
            h = 2
            host(win, h, score, "Good evening everyone my name is Steve Harvey and welcome to")
            host(win, h, score, "Family Feud!!")
            h = 1
            host(win, h, score, "Oh no, looks like I booted up one of the old files used to build the game")
            host(win, h, score, "Just play along while I try to get our game back")
            h = 2
            host(win, h, score, "Alright everyone, let's begin")
            host(win, h, score, "A random survey of 100 people were asked")
            score = FF(win, "What is your favorite room?", "Bathroom", "Livingroom", "Dinningroom", "Bedroom", "Ballroom", "Dressingroom", "Storageroom", "Weightroom", "Dungeon", "Courtyard", "Outside", "q", score)
            score = FF(win, "What is normally found in your pockets?", "Wallet", "Keys", "Phone", "Money", "Pencil/Pen", "Luckey Charm", "'Raincoat'", "Change", "Writing Pad", "Credit Card", "Knife", "e", score)
            score = FF(win, "What animal is considered the scariest?", "Snakes", "Spiders", "Allegators", "Falcons", "Lions", "Tigers", "Bears", "Ducks", "Cockroaches", "Oh my", "Ants", "w", score)
            h = 1
            host(win, h, score, "Ok, I think I got it")
            host(win, h, score, "Let's just")
            win.setBackground("black")
            time.sleep(2)
            win.setBackground("light blue")
            host(win, h, score, "That should do it, now-")
            h = 3
            host(win, h, score, "And heres your host, Alex Trebek")
            h = 1
            host(win, h, score, "...Alright, I'm going to try and get the right game back, Just play along")
            h = 9
            host(win, h, score, "This game has the possible points that can be earned at the top")
            h = 3
            host(win, h, score, "Here are the catagories")
            score = Jep(win, 100, "He invented the light bulb and patented 100+ other inventions", "Who is...", "Einstein", "Tesla", "Batman", "Elon Musk", "q", score)
            score = Jep(win, 200, "Home of the president of the U.S., This place also houses the Washington Monument", "Where is...", "Maine", "Vermont", "Maryland", "Washington D.C", "r", score)
            score = Jep(win, 300, "This animal uses its long tounge and hard beak to reach bugs inside of tree", "What is...", "A Peacock", "An Eagles", "A Woodpecker", "A Duck", "e", score)
            h = 1
            host(win, h, score, "I think I have the right one this time")
            win.setBackground("black")
            time.sleep(2)
            win.setBackground("light blue")
            host(win, h, score, "Is that it?")
            host(win, h, score, "I don't hear anything")
            host(win, h, score, "Good, were back, now-")
            h = 4
            host(win, h, score, "Are you smarter than a 5th Grader!!!")
            h = 1
            host(win, h, score, "...")
            h = 9
            host(win, h, score, "This game includes a hint option where one of the kids help you out for half of the points (now 100)")
            h = 4
            host(win, h, score, "Let's play!")
            score = s5thgrader(win, "How many feet are in a mile?", "5 tomatos", "4036", "2080", "5280", "3089", "e", score)
            score = s5thgrader(win, "What is 100 / 10?", "1 zero", "25", "110", "90", "10", "r", score)
            score = s5thgrader(win, "How many sides a triangle have?", "tri = 3", "3", "1", "4", "0", "q", score)
            score = s5thgrader(win, "What is the sun?", "A hot ball of gas", "A Planet", "A Star", "A Lightbulb", "Cheddar Cheese", "w", score)
            h = 1
            host(win, h, score, "Third times a charm, right")
            win.setBackground("black")
            time.sleep(2)
            win.setBackground("light blue")
            host(win, h, score, "Are we back?")
            host(win, h, score, "now-")
            time.sleep(3)
            host(win, h, score, "Alright, were back")
            host(win, h, score, "..And out of time, great")
            host(win, h, score, "Well, lets see how you did")
            h = 9
            score = host(win, h, score, ("Your score was: ", score))
            h = 1
            host(win, h, score, "Wow, thats a great score")
            h = 9
            host(win, h, score, "Note: Y.A.S.H cannot see score")
            h = 1
            host(win, h, score, "Thanks for playing, see you next time")
            plays += 1

if __name__ == "__main__":
    main() 

 
