# Mars/Moon lander psg Trial 1.0
# 2-2-24 David Nalywajko

# libraries
import PySimpleGUI as psg
import time

# constants
weight = 0
fuel = 0
oxygen = 0
speed = 0
elevation = 0
thrusterToggle = False
parachuteReleased = False

# graph setup
graph=psg.Graph(canvas_size=(300,900), graph_bottom_left=(0, -1000), graph_top_right=(10000,30000),
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
# column2 setup with graph and anything else we wanna add
column2 = [
    [graph]
    #[psg.Button('LEFT'), psg.Button('RIGHT'), psg.Button('UP'), psg.Button('DOWN')]
]
# layout puts the window layout together an window instantiates the window
layout = [[psg.Column(column1), psg.VSeparator(), psg.Column(column2)]]
window = psg.Window('Penguin Lander', layout, finalize=True)

# rocket starting location and instantiation of rocket and moon
x1,y1 = 5000,15000
rocket = graph.draw_circle((x1,y1), 100, fill_color='black', line_color='white')
moon = graph.draw_rectangle((10000,1000), (0,-1000), line_color='grey', fill_color='grey')

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
        print("thrusters: " + str(thrusterToggle))
    if event == 'Parachute': # Parachute button pushed
        parachuteReleased = True
    '''
    if event == 'RIGHT':
        graph.MoveFigure(rocket, 100, 0)
    if event == 'LEFT':
        graph.MoveFigure(rocket, -100,0)
    if event == 'UP':
        graph.MoveFigure(rocket, 0, 100)
    if event == 'DOWN':
        graph.MoveFigure(rocket, 0,-100)
    if event=="graph+UP":
        x2,y2= values['graph']
        graph.MoveFigure(rocket, x2-x1, y2-y1)
        x1,y1=x2,y2
    '''
      
window.close()
