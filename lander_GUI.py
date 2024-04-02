# Mars/Moon lander psg version 2
# 2-16-24 David Nalywajko

# libraries
import PySimpleGUI as psg
from random import randrange
import lander_Physics as controller

#music
import winsound
winsound.PlaySound("holst_mars.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )

# variables
time_elapsed = 0
startingHeight = 100000 # m
screenHeight = 100000 # m
altitude = startingHeight
m_fuel = 3000 # kg 4000  8165 + 2268
m_lander = 3000 # 5000  kg 2152 + 2353
velocity = -200 # m/s
positionChange = 0 # m
impactTime = 999 # s
acceleration = -2.607 # m/s^2
thrusterToggle = False
parachuteReleased = False
automatedLanding = False

moon = controller.Planet(6.67430*10**(-11), 7.34767309*10**22, 1740000.0)
rocket = controller.Lander(altitude = startingHeight, velocity = velocity, mass_fuel = m_fuel, mass_lander = m_lander, F_thrust = 16000, fuel_consumption = 10, planet = moon)

rocket.newTable(time_elapsed, altitude, velocity, m_fuel, m_lander, positionChange, acceleration, impactTime) # Make a new blackboard for trial

isRunning = True
speed = 20 #1000 is 1 sec (default)


# set theme
psg.theme('DarkBlue13')

# graph setup
graph=psg.Graph(canvas_size=(300,900), graph_bottom_left=(0, -1000),
    graph_top_right=((screenHeight/3), (screenHeight+screenHeight/80)),
    background_color='black', enable_events=True, drag_submits=True, key='graph')
# column1 setup with text and buttons
column1 = [
    [psg.Text("Altitude:"), psg.Text(str(altitude) + " m", key="altitudetxt")],
    [psg.Text("Fuel Remaining:"), psg.Text(f"{round(m_fuel, 2):.2f}" + " kg", key="fueltxt")],
    [psg.Text("Total Weight:"), psg.Text(str(m_lander) + " kg", key="weighttxt")],
    [psg.Text("Velocity:"), psg.Text(str(velocity) + " m/s", key="velocitytxt")],
    [psg.Text("Time until Impact:"), psg.Text(str(impactTime) + " s", key="impacttimetxt")],
    [psg.Graph((20, 20), (0, 0), (20, 20), key="thrustersdot"), psg.Button("Thrusters")],
    [psg.Graph((20, 20), (0, 0), (20, 20), key="parachutesdot"), psg.Button("Parachute")],
    [psg.Graph((20, 20), (0, 0), (20, 20), key="automatedlandingdot"), psg.Button("Automated Landing")],
]
# column2 setup with graph and anything else we want to add
column2 = [
    [graph]
]
# layout puts the window layout together and window instantiates the window
layout = [[psg.Column(column1), psg.VSeparator(), psg.Column(column2)]]
window = psg.Window('Penguin Lander', layout, finalize=True)

# bind keys
window.bind('<space>', 'Thrusters')
window.bind('<p>', 'Parachute')
window.bind('<a>', 'Automated Landing')

# objects on the graph
rocketTop = graph.DrawPolygon(((screenHeight/6-500, startingHeight + 2000),
    (screenHeight/6+500, startingHeight + 2000), (screenHeight/6, startingHeight + 2800)),
    fill_color='blue', line_color='#7184a8')
rocketMiddle = graph.DrawRectangle((screenHeight/6-500, startingHeight + 2000),
    (screenHeight/6+500, startingHeight), fill_color='blue', line_color='#7184a8')
rocketBottom = graph.DrawPolygon(((screenHeight/6-900, startingHeight - 600),
    (screenHeight/6, startingHeight + 2500), (screenHeight/6+950, startingHeight - 600),
    (screenHeight/6, startingHeight-100)), fill_color='blue', line_color='#7184a8')
flame = graph.DrawOval((screenHeight/6-300,startingHeight),
    (screenHeight/6+300, startingHeight-1800), fill_color="red", line_color="black")
moon = graph.draw_rectangle(((screenHeight/3),(screenHeight/30)),
    (0,(-screenHeight/30)), line_color='#767676', fill_color='#767676')
for stars in range(300):
    x,y = randrange(int(screenHeight/3)), randrange(int(screenHeight))
    star = graph.draw_circle((x, y), screenHeight/1000, line_color='white',  fill_color='white')
    graph.send_figure_to_back(star)
for craters in range(35):
    x,y = randrange(int(screenHeight/3)), screenHeight/40-randrange(int(screenHeight/30))
    crater = graph.draw_circle((x, y), (randrange(int(6))+3)*100,
        line_color='#444444',  fill_color='#676767')

# put shapes in right layers
graph.bring_figure_to_front(rocketBottom)
graph.bring_figure_to_front(rocketTop)
graph.bring_figure_to_front(rocketMiddle)

# functions we call every 1 second
def updateAltitude():
    altitude = rocket.getCurrentAltitude()
    # update altitude
    window['altitudetxt'].update(str(round(altitude, 2)) + " m")
    
def updateFuel():
    fuel = rocket.getFuel()
    # update fuel
    window['fueltxt'].update(f"{round(fuel, 2):.2f}" + " kg")
    
def updateWeight():
    total_mass = rocket.getMass() + m_fuel
    # update weight
    window['weighttxt'].update(str(round(total_mass, 2)) + " kg")
    
def updateVelocity():
    velocity = rocket.getCurrentLanderVelocity()
    # update velocity
    window['velocitytxt'].update(str(round(velocity, 2)) + " m/s")
    
def updateImpactTime():
    impactTime = rocket.getImpactTime()
    # update impact time
    window['impacttimetxt'].update(str(round(impactTime, 2)) + " s")
    
def moveRocket(thrusterToggle):
    positionChange = rocket.getDisplacement()
    # update visual position of rocket
    graph.MoveFigure(rocketTop, 0, positionChange)
    graph.MoveFigure(rocketMiddle, 0, positionChange)
    graph.MoveFigure(rocketBottom, 0, positionChange)
    graph.MoveFigure(flame, 0, positionChange)
def updateFlame(thrusterToggle):
    # make flame red if thrusters on or invisibly black if off
    if thrusterToggle:
        graph.Widget.itemconfig(flame, fill="red")
        graph.bring_figure_to_front(flame)
    else:
        graph.Widget.itemconfig(flame, fill="black")
        graph.send_figure_to_back(flame)

def collisionCheck():
    velocity = rocket.velocity
    altitude = rocket.altitude
    global isRunning
    
    if (altitude < 0):
        if (velocity > -5):
            #YAY
            endText = "YOU WIN!"
        else:
            #CRASH
            endText = "YOU DIED!"
            #BOOM
            graph.DrawCircle((screenHeight/6,0), 5000, fill_color="red", line_color="orange", line_width=10)
        print(endText)
        psg.popup_ok(endText, title="Game Over")
        isRunning = False
        



# infinite loop
while isRunning:
    # line 1 of loop waits 1 second and executes
    event, values = window.read(timeout = speed)
    
    # get any user inputs
    if event == psg.WIN_CLOSED:
        break # user closed the window
    
    if event == psg.TIMEOUT_KEY:
        pass # user didn't do anything
    

    # Automated Landing
    if automatedLanding == True:
        velocity = rocket.velocity
        altitude = rocket.altitude
        
        window['automatedlandingdot'].draw_circle((10, 10), 10, fill_color='green')
        if (velocity < (-1200 * ((altitude+2000)/screenHeight))*0.60):
            thrusterToggle = True
        elif ((altitude < 100) & (velocity < -5)):
            thrusterToggle = True
        else:
            thrusterToggle = False
    else:
        window['automatedlandingdot'].draw_circle((10, 10), 10, fill_color='red')
    

    if rocket.mass_fuel < 10:
        thrusterToggle = False
    elif event == 'Thrusters': # Thruster button pushed
        thrusterToggle = not thrusterToggle
       
    if event == 'Parachute': # Parachute button pushed
        parachuteReleased = True
        
    if event == 'Automated Landing': # Automated Landing button pushed
        automatedLanding = not automatedLanding


    # call functions
    rocket.getCurrentAcceleration(thrusterToggle)    
    updateAltitude()
    updateVelocity()
    updateImpactTime()
    moveRocket(thrusterToggle)
    updateFlame(thrusterToggle)
    acceleration = rocket.getCurrentAcceleration(thrusterToggle)

    if (thrusterToggle):
        window['thrustersdot'].draw_circle((10, 10), 10, fill_color='green')
        updateFuel()
    else:
        window['thrustersdot'].draw_circle((10, 10), 10, fill_color='red')
        
    updateWeight()

    collisionCheck()

    time_elapsed += 1
    rocket.addRow(time_elapsed)
    
window.close()
