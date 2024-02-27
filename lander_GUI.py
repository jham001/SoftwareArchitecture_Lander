# Mars/Moon lander psg version 2
# 2-16-24 David Nalywajko

# libraries
import PySimpleGUI as psg
from random import randrange
import lander_Physics as physics

# variables
startingHeight = 100000
Ialtitude = startingHeight
Ifuel = 4000
Iweight = 5000
Ivelocity = 200
IimpactTime = 100
thrusterToggle = False
parachuteReleased = False
physics.newTable() # Make a new blackboard for trial

# set theme
psg.theme('DarkBlue13')

# graph setup
graph=psg.Graph(canvas_size=(300,900), graph_bottom_left=(0, -1000),
    graph_top_right=((startingHeight/3), (startingHeight+startingHeight/80)),
    background_color='black', enable_events=True, drag_submits=True, key='graph')
# column1 setup with text and buttons
column1 = [
    [psg.Text("Altitude:"), psg.Text(str(Ialtitude) + " m", key="altitudetxt")],
    [psg.Text("Fuel Remaining:"), psg.Text(str(Ifuel) + " kg", key="fueltxt")],
    [psg.Text("Total Weight:"), psg.Text(str(Iweight) + " kg", key="weighttxt")],
    [psg.Text("Velocity:"), psg.Text(str(Ivelocity) + " m/s", key="velocitytxt")],
    [psg.Text("Time until Impact:"), psg.Text(str(IimpactTime) + " s", key="impacttimetxt")],
    [psg.Button("Thrusters")],
    [psg.Button("Parachute")],
]
# column2 setup with graph and anything else we want to add
column2 = [
    [graph]
]
# layout puts the window layout together and window instantiates the window
layout = [[psg.Column(column1), psg.VSeparator(), psg.Column(column2)]]
window = psg.Window('Penguin Lander', layout, finalize=True)

# objects on the graph
rocketTop = graph.DrawPolygon(((startingHeight/6-500, startingHeight + 1000),
    (startingHeight/6+500, startingHeight + 1000), (startingHeight/6, startingHeight + 1800)),
    fill_color='blue', line_color='#ECDEC9')
rocketMiddle = graph.DrawRectangle((startingHeight/6-500, startingHeight + 1000),
    (startingHeight/6+500, startingHeight-1000), fill_color='blue', line_color='#ECDEC9')
rocketBottom = graph.DrawPolygon(((startingHeight/6-900, startingHeight - 1600),
    (startingHeight/6, startingHeight + 1800), (startingHeight/6+950, startingHeight - 1600),
    (startingHeight/6, startingHeight-1100)), fill_color='blue', line_color='#ECDEC9')
moon = graph.draw_rectangle(((startingHeight/3),(startingHeight/30)),
    (0,(-startingHeight/30)), line_color='grey', fill_color='grey')
for stars in range(300):
    x,y = randrange(int(startingHeight/3)), randrange(int(startingHeight))
    star = graph.draw_circle((x, y), startingHeight/1000, line_color='white',  fill_color='white')
    graph.send_figure_to_back(star)
for craters in range(35):
    x,y = randrange(int(startingHeight/3)), startingHeight/40-randrange(int(startingHeight/30))
    crater = graph.draw_circle((x, y), (randrange(int(6))+3)*100,
        line_color='#333333',  fill_color='#767676')

# put shapes in right layers
graph.bring_figure_to_front(rocketBottom)
graph.bring_figure_to_front(rocketTop)
graph.bring_figure_to_front(rocketMiddle)

# random functions
def is_thrust_on():
    return thrusterToggle

# functions we call every 1 second
def updateAltitude(thrusterToggle):
    # get new altitude
        #altitude = 42
    altitude = physics.getCurrentAltitude(thrusterToggle)
    # update altitude
    window['altitudetxt'].update(str(altitude) + " m")
    
def updateFuel():
    # get new fuel
        #fuel = 69
    fuel = physics.getFuel()
    # update fuel
    window['fueltxt'].update(str(fuel) + " kg")
    
def updateWeight():
    # get new weight
        #weight = 96
    weight = physics.getMass()
    # update weight
    window['weighttxt'].update(str(weight) + " kg")
    
def updateVelocity(thrusterToggle):
    # get new velocity
        #velocity = 456
    velocity = physics.getCurrentLanderVelocity(thrusterToggle)
    # update velocity
    window['velocitytxt'].update(str(velocity) + " m/s")
    
def updateImpactTime():
    # get new impact time
        #impactTime = 789
    impactTime = physics.getImpactTime()
    # update impact time
    window['impacttimetxt'].update(str(impactTime) + " s")
    
def moveRocket(thrusterToggle):
    # get change in position
    #if thrusterToggle == True:
    #    positionChange = -200
    #else:
    #    positionChange = -400
    positionChange = physics.getDisplacement(thrusterToggle)
    # update visual position of rocket
    graph.MoveFigure(rocketTop, 0, positionChange)
    graph.MoveFigure(rocketMiddle, 0, positionChange)
    graph.MoveFigure(rocketBottom, 0, positionChange)

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
    updateAltitude(thrusterToggle)
    updateFuel()
    updateWeight()
    updateVelocity(thrusterToggle)
    updateImpactTime()
    moveRocket(thrusterToggle)
    
window.close()
