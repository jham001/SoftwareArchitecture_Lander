# Mars/Moon lander psg version 2
# 2-16-24 David Nalywajko
# 00-00-00 Comments by Nicholas Balarezo

#libraries
import PySimpleGUI as psg                       # for graphics
from random import randrange                    # for distribution of stars/craters
import lander_Physics as controller             # physics and planet server controller
import lander_AutoLand_controller as autoland   # autoland function exernal server
import winsound                                 # for music

#GAME WINDOW FUNCTION
def run(startingHeight, mass_fuel, mass_lander, velocity, F_thrust, fuel_consumption, speed):
    winsound.PlaySound("holst_mars.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )

    #variables 
    time_elapsed = 0
    screenHeight = 100000 # m
    positionChange = 0 # m
    impactTime = 999 # s
    acceleration = -2.607 # m/s^2
    thrusterToggle = False
    #parachuteReleased = False
    automatedLanding = False

    #begin moon server and rocket server, moon and rocket objects get instantiated
    moon = controller.Planet(6.67430*10**(-11), 7.34767309*10**22, 1740000.0)
    rocket = controller.Lander(altitude = startingHeight, velocity = velocity, mass_fuel = mass_fuel, mass_lander = mass_lander, F_thrust =  F_thrust, fuel_consumption = fuel_consumption, planet = moon)
    #creates a new table for the database
    rocket.newTable(time_elapsed, startingHeight, velocity, mass_fuel, mass_lander, positionChange, acceleration, impactTime) # Make a new blackboard for trial

    #declare isRunning variable
    global isRunning
    #initialize to true so game loop can run
    isRunning = True

    #SET THEME
    psg.theme('DarkBlue13')

    #GRAPH SETUP
    #create graph
    graph=psg.Graph(canvas_size=(300,900), graph_bottom_left=(0, -1000),
        graph_top_right=((screenHeight/3), (screenHeight+screenHeight/80)),
        background_color='black', enable_events=True, drag_submits=True, key='graph')
    #column1 setup with text and buttons
    column1 = [
        #create text areas and display variables as information from blackboard
        [psg.Text("Altitude:"), psg.Text(str(startingHeight) + " m", key="altitudetxt")],
        [psg.Text("Fuel Remaining:"), psg.Text(f"{round(mass_fuel, 2):.2f}" + " kg", key="fueltxt")],
        [psg.Text("Total Weight:"), psg.Text(str(mass_lander) + " kg", key="weighttxt")],
        [psg.Text("Velocity:"), psg.Text(str(velocity) + " m/s", key="velocitytxt")],
        [psg.Text("Time until Impact:"), psg.Text(str(impactTime) + " s", key="impacttimetxt")],
        #create lights (graphs) and buttons in left display screen
        [psg.Graph((20, 20), (0, 0), (20, 20), key="thrustersdot"), psg.Button("Thrusters")],
        #[psg.Graph((20, 20), (0, 0), (20, 20), key="parachutesdot"), psg.Button("Parachute")],
        [psg.Graph((20, 20), (0, 0), (20, 20), key="automatedlandingdot"), psg.Button("Automated Landing")],
        [psg.Text("\t\t\t\t")] # this puts a buffer that stops the screen from resizing
    ]
    #column2 setup with graph and anything else we want to add
    column2 = [
        [graph]
    ]
    #layout puts the window layout together and window instantiates the window
    layout = [[psg.Column(column1), psg.VSeparator(), psg.Column(column2)]]
    window = psg.Window('Penguin Lander', layout, finalize=True)

    #bind keys
    window.bind('<space>', 'Thrusters')
    #window.bind('<p>', 'Parachute')
    window.bind('<a>', 'Automated Landing')

    #objects on the graph, a.k.a rocket graphics
    #rocket top
    rocketTop = graph.DrawPolygon(((screenHeight/6-500, startingHeight + 2000),
        (screenHeight/6+500, startingHeight + 2000), (screenHeight/6, startingHeight + 2800)),
        fill_color='blue', line_color='#7184a8')
    #rocket middle
    rocketMiddle = graph.DrawRectangle((screenHeight/6-500, startingHeight + 2000),
        (screenHeight/6+500, startingHeight), fill_color='blue', line_color='#7184a8')
    #rocket bottom
    rocketBottom = graph.DrawPolygon(((screenHeight/6-900, startingHeight - 600),
        (screenHeight/6, startingHeight + 2500), (screenHeight/6+950, startingHeight - 600),
        (screenHeight/6, startingHeight-100)), fill_color='blue', line_color='#7184a8')
    #flame
    flame = graph.DrawOval((screenHeight/6-300,startingHeight),
        (screenHeight/6+300, startingHeight-1800), fill_color="red", line_color="black")
    #moon
    moon = graph.draw_rectangle(((screenHeight/3),(screenHeight/30)),
        (0,(-screenHeight/30)), line_color='#767676', fill_color='#767676')
    #for loop generates stars randomly
    for stars in range(300):
        x,y = randrange(int(screenHeight/3)), randrange(int(screenHeight))
        star = graph.draw_circle((x, y), screenHeight/1000, line_color='white',  fill_color='white')
        graph.send_figure_to_back(star)
    #for loop generates craters randomly
    for craters in range(35):
        x,y = randrange(int(screenHeight/3)), screenHeight/40-randrange(int(screenHeight/30))
        crater = graph.draw_circle((x, y), (randrange(int(6))+3)*100,
            line_color='#444444',  fill_color='#676767')

    #put shapes in right layers
    graph.bring_figure_to_front(rocketBottom)
    graph.bring_figure_to_front(rocketTop)
    graph.bring_figure_to_front(rocketMiddle)
    #offset the rocket visually by the height of the moon so that the rocket appears to land on the moon surface
    #does not change the actual database/display values
    graph.MoveFigure(rocketTop, 0, 650 + (screenHeight/30))
    graph.MoveFigure(rocketMiddle, 0, 650 + (screenHeight/30))
    graph.MoveFigure(rocketBottom, 0, 650 + (screenHeight/30))
    graph.MoveFigure(flame, 0, 650 + (screenHeight/30))
    #functions we call every 1 second
    def updateAltitude():
        altitude = rocket.getCurrentAltitude()
        #update altitude
        window['altitudetxt'].update(str(round(altitude, 2)) + " m")
    
    #updates the weight being displayed on the sidebar of the main game window
    def updateWeight():
        #fuel mass is updated
        fuel = rocket.getFuel()
        #update fuel
        window['fueltxt'].update(f"{round(fuel, 2):.2f}" + " kg")
        #total mass is calculated and updated
        total_mass = rocket.getMass() + rocket.getFuel()
        #update weight being displayed
        window['weighttxt'].update(str(round(total_mass, 2)) + " kg")

    #updates the velocity being displayed on the sidebar of the main game window
    def updateVelocity():
        #current velocity is stored in a variable
        velocity = rocket.getCurrentLanderVelocity()
        #update velocity being displayed
        window['velocitytxt'].update(str(round(velocity, 2)) + " m/s")
    
    #updates the impact time being displayed on the sidebar of the main game window
    def updateImpactTime():
        #current impact time is stored in a variable
        impactTime = rocket.getImpactTime()
        #update impact time being displayed
        window['impacttimetxt'].update(str(round(impactTime, 2)) + " s")
    
    #updates the visual rocket position in the main game window
    def moveRocket(thrusterToggle):
        #displacement of the rocket is stored in the positionChange variable
        positionChange = rocket.getDisplacement()
        #update visual position of rocket
        graph.MoveFigure(rocketTop, 0, positionChange)
        graph.MoveFigure(rocketMiddle, 0, positionChange)
        graph.MoveFigure(rocketBottom, 0, positionChange)
        graph.MoveFigure(flame, 0, positionChange)
    
    #function to update flame depending on toggle status in a given moment
    def updateFlame(thrusterToggle):
        #if the thruster is toggled then make the flame red and bring it to the front
        if thrusterToggle:
            graph.Widget.itemconfig(flame, fill="red")
            graph.bring_figure_to_front(flame)
        #otherwise make it black and send it behind the graph
        else:
            graph.Widget.itemconfig(flame, fill="black")
            graph.send_figure_to_back(flame)

    #function to check if the rocket collides with altitude 0
    def collisionCheck():
        #temporary variables that store rocket velocity and altitude
        velocity = rocket.velocity
        altitude = rocket.altitude
        #check if rocket crashed
        if (altitude < 0):
            #isRunning used for main program loop
            global isRunning 
            #set isRunning variable to false so main program loop stops running
            isRunning= False
            if (velocity > -5):
                #end text set to success message
                endText = "SUCCESS!"
            else:
                #end text set to crash message
                endText = "YOU CRASHED..."
                #create an explosion figure/model that covers the rocket if the user crashes the rocket
                graph.DrawCircle((screenHeight/6,0), 5000, fill_color="red", line_color="orange", line_width=10)
            #print end text in console
            print(endText)
            #display a popup window containing endtext message
            psg.popup_ok(endText, title="Game Over")
    

    # MAIN PROGRAM LOOP
    while isRunning:
        #line 1 of loop waits 1 unit of time and executes
        event, values = window.read(timeout = speed) # 1000 for one second per second
    
        #get any user inputs
        #if user closed the window, break the loop
        if event == psg.WIN_CLOSED:
            break 
    
        #if user does nothing, continue the loop
        if event == psg.TIMEOUT_KEY:
            pass 

        #AUTOMATED LANDING
        #if automatedLanding toggle is true selects automated landing
        #a.k.a if button was pressed and var becomes true
        if automatedLanding == True:
            #set the automated landing status indicator light to green
            window['automatedlandingdot'].draw_circle((10, 10), 10, fill_color='green')
            #toggles thruster according to autoland function return value
            thrusterToggle = autoland.autoLand(velocity = rocket.velocity, altitude = rocket.altitude, screenHeight=screenHeight)
        #if automated landing is not selected
        else:
            #set the automated landing status indicator light to red
            window['automatedlandingdot'].draw_circle((10, 10), 10, fill_color='red')
        

        #THRUSTER FUNCTIONALITY
        #if rocket fuel mass is less than the fuel consumed per burn iteration, 
        #a.k.a check to see if fuel has run out 
        if rocket.mass_fuel < fuel_consumption:
            #thrusterToggle is false
            thrusterToggle = False
        #thruster button is pushed
        elif event == 'Thrusters': 
            thrusterToggle = not thrusterToggle
       
        #PARACHUTE (NOT INCLUDED, MOON HAS NO ATMOSPHERE TO WORK WITH)
        #if event == 'Parachute': # Parachute button pushed
            #parachuteReleased = True
        
        #AUTOMATED LANDING FUNCTIONALITY
        #if the automated landing button is pressed
        if event == 'Automated Landing':
            #automatedLanding is set to opposite of what it is at the momen the button is pressed
            automatedLanding = not automatedLanding

        #MAIN FUNCTION CALLS
        rocket.getCurrentAcceleration(thrusterToggle)    
        updateAltitude()
        updateVelocity()
        updateImpactTime()
        moveRocket(thrusterToggle)
        updateFlame(thrusterToggle)

        #if thruster is toggled
        if (thrusterToggle):
            #set the thruster status indicator light to green
            window['thrustersdot'].draw_circle((10, 10), 10, fill_color='green')
            #weight updates as fuel is burned
            updateWeight()
        #if thruster is not toggled
        else:
            #set the thruster status indicator light to red
            window['thrustersdot'].draw_circle((10, 10), 10, fill_color='red')
        
        #increment time by 1
        time_elapsed += 1
        #new row with current information is stored in database 
        rocket.addRow(time_elapsed)

        #check if rocket crashed/landed
        collisionCheck()
    
    #close window and rocket when loop ends
    #closes either when window is closed manually or rocket makes a collision
    window.close()
    rocket.close()