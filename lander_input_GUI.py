import PySimpleGUI as psg
import lander_GUI as game


inputColumn1 = [
    [psg.Text("Rocket Mass:")],
    [psg.Text("Rocket Fuel:")],
    [psg.Text("Starting Height")],
    [psg.Text("Starting Velocity")],
    [psg.Text("Force Thrust")],
    [psg.Text("Consumption Fuel")],
    [psg.Text("Simulation Speed")],
   
]

inputColumn2=[
    [psg.InputText('', enable_events=True, key='m_lander_input', justification='left')],
    [psg.InputText('', enable_events=True, key='f_lander_input', justification='left')],
    [psg.InputText('', enable_events=True, key='start_h_input', justification='left')],
    [psg.InputText('', enable_events=True, key='start_v_input', justification='left')],
    [psg.InputText('', enable_events=True, key='forceThrust_input', justification='left')],
    [psg.InputText('', enable_events=True, key='consumption_fuel_input', justification='left')],
    [psg.InputText('', enable_events=True, key='simulation_speed_input', justification='left')],
]
bottomRow=[[psg.Button("Land this penguin!")]]

# layout puts the window layout together and window instantiates the window
layout = [[psg.Column(inputColumn1), psg.VSeparator(), psg.Column(inputColumn2)],[psg.Column(bottomRow)]]
window = psg.Window('Input Value Window', layout, finalize=True)

isRunning = True

# Predefined values
predefined_values = {
    'm_lander_input': '3000',  
    'f_lander_input': '3000', 
    'start_h_input': '100000', 
    'start_v_input': '-200',  
    'forceThrust_input': '16000',
    'consumption_fuel_input': '10',  
    'simulation_speed_input': '50'  
}

# Update input fields with predefined values
for key, value in predefined_values.items():
    window[key].update(value)

# Update input fields with predefined values
for key, value in predefined_values.items():
    window[key].update(value)

while isRunning:
    # line 1 of loop waits 1 second and executes
    event, values = window.read(timeout = 1000)
    
    # get any user inputs
    if event == psg.WIN_CLOSED:
        break # user closed the window
    
    if event == psg.TIMEOUT_KEY:
        pass # user didn't do anything

    if event == "Land this penguin!":
        isRunning = False;
        window.close() # Form Submitted

    if event == 'm_lander_input':
        if values['m_lander_input'] and not values['m_lander_input'].isdigit():
            psg.popup("Only digits allowed")
            window['m_lander_input'].update(values['m_lander_input'][:-1])

    if event == 'f_lander_input':
        if values['f_lander_input'] and not values['f_lander_input'].isdigit():
            psg.popup("Only digits allowed")
            window['f_lander_input'].update(values['f_lander_input'][:-1])

    if event == 'start_h_input':
        if values['start_h_input'] and not values['start_h_input'].isdigit():
            psg.popup("Only digits allowed")
            window['start_h_input'].update(values['start_h_input'][:-1])

    if event == 'start_v_input':
        input_text = values['start_v_input']
        if input_text and not ((input_text == '-' and len(input_text) == 1) or (input_text.startswith('-') and input_text[1:].isdigit())):
            psg.popup("Only integers allowed")
            window['start_v_input'].update(input_text[:-1])

    if event == 'forceThrust_input':
        if values['forceThrust_input'] and not values['forceThrust_input'].isdigit():
            psg.popup("Only digits allowed")
            window['forceThrust_input'].update(values['forceThrust_input'][:-1])

    if event == 'consumption_fuel_input':
        if values['consumption_fuel_input'] and not values['consumption_fuel_input'].isdigit():
            psg.popup("Only digits allowed")
            window['consumption_fuel_input'].update(values['consumption_fuel_input'][:-1])

    if event == 'simulation_speed_input':
        if values['simulation_speed_input'] and not values['simulation_speed_input'].isdigit():
            psg.popup("Only digits allowed")
            window['simulation_speed_input'].update(values['simulation_speed_input'][:-1])

# Convert values to integers
# Replace '-' with '0' if the value is just '-'
values = {key: ('0' if value == '-' else value) for key, value in values.items()}

# Convert values to integers
values = {key: int(value) for key, value in values.items()}

# Launch lander_GUI.py with data
game.run(startingHeight=values['start_h_input'], velocity=values['start_v_input'],
         mass_fuel=values['f_lander_input'], mass_lander=values['m_lander_input'],
         F_thrust=values['forceThrust_input'], fuel_consumption=values['consumption_fuel_input'], speed=values['simulation_speed_input'])