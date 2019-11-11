from graphics import *
import time
import random
from Question_Layout import layout
import Start_Screen 
from Special_Layouts import FF

w = 1000
h = 650
win = GraphWin("Brain Flex the game", w , h)
win.setCoords(0.0 ,0.0 ,100.0, 100.0)
win.setBackground("light blue")
g = 0
y1 = random.random() * 100
y2 = y1 + 3
x1 = random.random() * 100
x2 = x1 + 3

Start_Screen.Starting(win)
score, y1, y2, x1, x2 = layout(win, g, y1, y2, x1, x2, "What is the square root of 81?", "3", "7", "9", "What's a square root?", "e", 0)
g = 1
score, y1, y2, x1, x2 = layout(win, g, y1, y2, x1, x2, "What is the capital of Michigan?", "Detroit", "Kalamazoo", "Hell", "Lansing", "r", score)
score, y1, y2, x1, x2 = layout(win, g, y1, y2, x1, x2, "What is 106 times 6?", "636", "730", "630", "102", "q", score)
g = 0
score = FF(win, "What is your favorite room?", "Bathroom", "Livingroom", "Dinningroom", "Bedroom", "Ballroom", "Dressingroom", "Storageroom", "Weightroom", "Dungeon", "Courtyard", "Outside", "q", score)
