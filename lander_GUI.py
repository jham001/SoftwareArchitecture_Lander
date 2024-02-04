# Mars/Moon lander psg Trial 1.0
# 2-2-24 David Nalywajko

# libraries
import PySimpleGUI as psg
from random import randrange
import time

'''Example DB info

import sqlite3

dbVar = sqlite3.connect("path")

def getTable(someFile, dataIndex):
    sqlCommand = "SELECT * FROM TABLE"
    cursor = dbVar.execute(sqlCommand)
    for row in cursor:
        for entry in row
            return entry # would return TABLE
'''

# variables
startingHeight = 100000
weight = 0
fuel = 0
oxygen = 0
speed = 0
elevation = 0
thrusterToggle = False
parachuteReleased = False

# graph setup
graph=psg.Graph(canvas_size=(300,900), graph_bottom_left=(0, -1000),
    graph_top_right=((startingHeight/3), (startingHeight+startingHeight/100)),
    background_color='black', enable_events=True, drag_submits=True, key='graph')
# column1 setup with text and buttons
column1 = [
    [psg.Text("Ship Weight:"), psg.Text(str(weight) + " kg", key="weighttxt")],
    [psg.Text("Fuel Remaining:"), psg.Text(str(fuel) + " kg", key="fueltxt")],
    [psg.Text("Oxygen Remaining:"), psg.Text(str(oxygen) + " L", key="oxygentxt")],
    [psg.Text("Speed"), psg.Text(str(speed) + " m/s", key="speedtxt")],
    [psg.Text("Elevation"), psg.Text(str(elevation) + " m", key="elevationtxt")],
    [psg.Button("Thrusters")],
    [psg.Button("Parachute")],
]
# column2 setup with graph and anything else we want to add
column2 = [
    [graph]
]
# layout puts the window layout together an window instantiates the window
layout = [[psg.Column(column1), psg.VSeparator(), psg.Column(column2)]]
window = psg.Window('Penguin Lander', layout, finalize=True)

# objects on the graph
rocket = graph.draw_circle(((startingHeight/6),startingHeight), 1000,
    fill_color='red', line_color='white')
graph.bring_figure_to_front(rocket)
moon = graph.draw_rectangle(((startingHeight/3),(startingHeight/30)),
    (0,(-startingHeight/30)), line_color='grey', fill_color='grey')
for stars in range(300):
    x,y = randrange(int(startingHeight/3)), randrange(int(startingHeight))
    star = graph.draw_circle((x, y), 100, line_color='white',  fill_color='white')
    graph.send_figure_to_back(star)
for craters in range(40):
    x,y = randrange(int(startingHeight/3)), startingHeight/40-randrange(int(startingHeight/30))
    crater = graph.draw_circle((x, y), randrange(int(6)+3)*100, line_color='#333333',  fill_color='#767676')

# functions we call every 1 second
def moveRocket():
    if thrusterToggle == True:
        graph.MoveFigure(rocket, 0,-100)
    else:
        graph.MoveFigure(rocket, 0,-200)
def updateFuel():
    pass
def updateOxygen():
    pass
def updateSpeed():
    pass
def updateElevation():
    pass

# infinite loop
while True:
    # line 1 of loop waits 1 second and executes
    event, values = window.read(timeout = 1000)
    
    # call functions
    moveRocket()
    updateFuel()
    updateOxygen()
    updateSpeed()
    updateElevation()
    
    # get any user inputs
    if event == psg.WIN_CLOSED:
        break # user closed the window
    if event == psg.TIMEOUT_KEY:
        pass # user didn't do anything
    if event == 'Thrusters': # Thruster button pushed
        thrusterToggle = not thrusterToggle
    if event == 'Parachute': # Parachute button pushed
        parachuteReleased = True

window.close()
