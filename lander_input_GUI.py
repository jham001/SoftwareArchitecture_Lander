import PySimpleGUI as psg
import lander_GUI as game
#RUN THIS FILE

#Scenarios
#Lander only with some instruments
#Lander with Rover for experiments
#Lander with 1 and 2 astronauts

#CREATE UI/FORM FOR INITIAL VALUE INPUTS
#create column 1 to denote input field labels
inputColumn1 = [
    [psg.Text("Rocket Mass:")],
    [psg.Text("Rocket Fuel:")],
    [psg.Text("Starting Height")],
    [psg.Text("Starting Velocity")],
    [psg.Text("Force Thrust")],
    [psg.Text("Consumption Fuel")],
    [psg.Text("Simulation Speed")],
   
]

#create column 2 for input fields
inputColumn2=[
    [psg.InputText('', enable_events=True, key='m_lander_input', justification='left')],
    [psg.InputText('', enable_events=True, key='f_lander_input', justification='left')],
    [psg.InputText('', enable_events=True, key='start_h_input', justification='left')],
    [psg.InputText('', enable_events=True, key='start_v_input', justification='left')],
    [psg.InputText('', enable_events=True, key='forceThrust_input', justification='left')],
    [psg.InputText('', enable_events=True, key='consumption_fuel_input', justification='left')],
    [psg.InputText('', enable_events=True, key='simulation_speed_input', justification='left')],
]

#create button to submit input field form
bottomRow=[[psg.Button("Land this penguin!")]]

#layout puts the window layout together
layout = [[psg.Column(inputColumn1), psg.VSeparator(), psg.Column(inputColumn2)],[psg.Column(bottomRow)]]
#window instantiates the window
window = psg.Window('Input Value Window', layout, finalize=True)

#set isRunning as true for the collection of data in the form
isRunning = True

#set defaults of initial value form as these predefined values
#fields will have these values predefined for a standard moon landing simulation
predefined_values = {
    'm_lander_input': '3000',  
    'f_lander_input': '3000', 
    'start_h_input': '100000', 
    'start_v_input': '-200',  
    'forceThrust_input': '16000',
    'consumption_fuel_input': '10',  
    'simulation_speed_input': '50'  
}


#define function that validates values in while loop
#this prevents erroneous values from breaking the lander function
def validateInputValues(event, values):
    #if the user changes the lander mass input then the input is validated as a number
    if event == 'm_lander_input':
        #if the user adds input and the input is not a digit
        if values['m_lander_input'] and not values['m_lander_input'].isdigit():
            #output the error message in a popup window
            psg.popup("Only digits allowed")
            #remove the content from the input field
            window['m_lander_input'].update(values['m_lander_input'][:-1])
    #if the user changes the fuel mass input then the input is validated as a number
    if event == 'f_lander_input':
        #if the user adds input and the input is not a digit
        if values['f_lander_input'] and not values['f_lander_input'].isdigit():
            #output the error message in a popup window
            psg.popup("Only digits allowed")
            #remove the content from the input field
            window['f_lander_input'].update(values['f_lander_input'][:-1])
    #if the user changes the starting height input then the input is validated as a number
    if event == 'start_h_input':
        #if the user adds input and the input is not a digit
        if values['start_h_input'] and not values['start_h_input'].isdigit():
            #output the error message in a popup window
            psg.popup("Only digits allowed")
            #remove the content from the input field
            window['start_h_input'].update(values['start_h_input'][:-1])
    #if the user changes the starting velocity input then the input is validated as a number
    if event == 'start_v_input':
        #stores user input as a new variable to differentiate the input string given its negative sign requirement
        input_text = values['start_v_input']
        #check that the user input begins with a negative sign and is a number
        if input_text and not ((input_text == '-' and len(input_text) == 1) or (input_text.startswith('-') and input_text[1:].isdigit())):
            #output the error message in a popup window
            psg.popup("Only negative integers allowed")
            #remove the content from the input field
            window['start_v_input'].update(input_text[:-1])
    #if the user changes the force thrust input then the input is validated as a number
    if event == 'forceThrust_input':
        #if the user adds input and the input is not a digit
        if values['forceThrust_input'] and not values['forceThrust_input'].isdigit():
            #output the error message in a popup window
            psg.popup("Only digits allowed")
            #remove the content from the input field
            window['forceThrust_input'].update(values['forceThrust_input'][:-1])
    #if the user changes the consumption fuel input then the input is validated as a number
    if event == 'consumption_fuel_input':
        #if the user adds input and the input is not a digit
        if values['consumption_fuel_input'] and not values['consumption_fuel_input'].isdigit():
            #output the error message in a popup window
            psg.popup("Only digits allowed")
            #remove the content from the input field
            window['consumption_fuel_input'].update(values['consumption_fuel_input'][:-1])
    #if the user changes the simulation speed input then the input is validated as a number
    if event == 'simulation_speed_input':
        #if the user adds input and the input is not a digit
        if values['simulation_speed_input'] and not values['simulation_speed_input'].isdigit():
            #output the error message in a popup window
            psg.popup("Only digits allowed")
            #remove the content from the input field
            window['simulation_speed_input'].update(values['simulation_speed_input'][:-1])


#update input fields with predefined values, a.k.a insert predefined values into form fields
for key, value in predefined_values.items():
    window[key].update(value)

#LOOP MAINTAINS THE WINDOW AS OPENED AND LISTENS FOR EVENTS, ALSO PROVIDES FORM VALIDATION
while isRunning:
    #line 1 of loop waits 1 second and executes, checks every second for events
    event, values = window.read(timeout = 1000)
    
    #if user closes the window then the initial window loop closes
    if event == psg.WIN_CLOSED:
        break
    
    #if the user does nothing the loop continues on
    if event == psg.TIMEOUT_KEY:
        pass
    #if user chooses to submit the form then the loop breaks and the window closes so the program may begin
    if event == "Land this penguin!":
        #break the loop and close the window
        isRunning = False
        window.close()
    #call function to validate all the values and prevent erroneous input
    validateInputValues(event, values)

#VALUE CONVERSION FOR MAIN PROGRAM
#Replace '-' with '0' if the value is just '-' or blank
values = {key: ('0' if (value == '-' or value == '') else value) for key, value in values.items()}

#Convert every other value to an integer
values = {key: int(value) for key, value in values.items()}

#LAUNCH lander_GUI.py WITH CONVERTED DATA
game.run(startingHeight=values['start_h_input'], velocity=values['start_v_input'],
         mass_fuel=values['f_lander_input'], mass_lander=values['m_lander_input'],
         F_thrust=values['forceThrust_input'], fuel_consumption=values['consumption_fuel_input'], speed=values['simulation_speed_input'])