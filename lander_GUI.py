# Mars/Moon lander psg Trial 1.0
# 2-2-24 David Nalywajko

# libraries
import PySimpleGUI as psg
from random import randrange

# variables
startingHeight = 100000
altitude = startingHeight
fuel = 4000
weight = 5000
velocity = 200
impactTime = 100
thrusterToggle = False
parachuteReleased = False

# set theme
psg.theme('DarkBlue13')

# graph setup
graph=psg.Graph(canvas_size=(300,900), graph_bottom_left=(0, -1000),
    graph_top_right=((startingHeight/3), (startingHeight+startingHeight/100)),
    background_color='black', enable_events=True, drag_submits=True, key='graph')
# column1 setup with text and buttons
column1 = [
    [psg.Text("Altitude:"), psg.Text(str(altitude) + " m", key="altitudetxt")],
    [psg.Text("Fuel Remaining:"), psg.Text(str(fuel) + " kg", key="fueltxt")],
    [psg.Text("Total Weight:"), psg.Text(str(weight) + " kg", key="weighttxt")],
    [psg.Text("Velocity:"), psg.Text(str(velocity) + " m/s", key="velocitytxt")],
    [psg.Text("Time until Impact:"), psg.Text(str(impactTime) + " s", key="impacttimetxt")],
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
for craters in range(35):
    x,y = randrange(int(startingHeight/3)), startingHeight/40-randrange(int(startingHeight/30))
    crater = graph.draw_circle((x, y), (randrange(int(6))+3)*100, line_color='#333333',  fill_color='#767676')

# functions we call every 1 second
def updateAltitude():
    # get new altitude
    
    # update altitude
    window['altitudetxt'].update(str(altitude) + " m")
def updateFuel():
    # get new fuel
    
    # update fuel
    window['fueltxt'].update(str(fuel) + " kg")
def updateWeight():
    # get new weight
    
    # update weight
    window['weighttxt'].update(str(weight) + " kg")
def updateVelocity():
    # get new velocity
    
    # update velocity
    window['velocitytxt'].update(str(velocity) + " m/s")
def updateImpactTime():
    # get new impact time
    
    # update impact time
    window['impacttimetxt'].update(str(impactTime) + " s")
def moveRocket():
    if thrusterToggle == True:
        graph.MoveFigure(rocket, 0,-100)
    else:
        graph.MoveFigure(rocket, 0,-200)

# infinite loop
while True:
    # line 1 of loop waits 1 second and executes
    event, values = window.read(timeout = 1000)
    
    # get any user inputs
    if event == psg.WIN_CLOSED:
        break # user closed the window
    if event == psg.TIMEOUT_KEY:
        pass # user didn't do anything
    if event == 'Thrusters': # Thruster button pushed
        thrusterToggle = not thrusterToggle
    if event == 'Parachute': # Parachute button pushed
        parachuteReleased = True
    
    # call functions
    updateAltitude()
    updateFuel()
    updateWeight()
    updateVelocity()
    updateImpactTime()
    moveRocket()
    
window.close()
