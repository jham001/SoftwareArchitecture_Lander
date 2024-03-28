import PySimpleGUI as psg


inputColumn1 = [
    [psg.Text("Rocket Mass:")],
    [psg.Text("Starting Height")],
    [psg.Text("Starting Velocity")],
    [psg.Text("Force Thrust")],
    [psg.Text("Consumption Fuel")],
    [psg.Text("Simulation Speed")],
   
]

inputColumn2=[
    [psg.InputText('', enable_events=True, key='m_lander_input', justification='left')],
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

while isRunning:
    # line 1 of loop waits 1 second and executes
    event, values = window.read(timeout = 1000)
    
    # get any user inputs
    if event == psg.WIN_CLOSED:
        break # user closed the window
    
    if event == psg.TIMEOUT_KEY:
        pass # user didn't do anything

    if event == "Land this penguin!":
        break # user closed the window

    if event == 'm_lander_input':
      if values['m_lander_input'][-1] not in ('0123456789'):
         psg.popup("Only digits allowed")
         window['m_lander_input'].update(values['m_lander_input'][:-1])

    if event == 'start_h_input':
      if values['start_h_input'][-1] not in ('0123456789'):
         psg.popup("Only digits allowed")
         window['start_h_input'].update(values['start_h_input'][:-1])

    if event == 'start_v_input':
      if values['start_v_input'][-1] not in ('0123456789'):
         psg.popup("Only digits allowed")
         window['start_v_input'].update(values['start_v_input'][:-1])

    if event == 'forceThrust_input':
      if values['forceThrust_input'][-1] not in ('0123456789'):
         psg.popup("Only digits allowed")
         window['forceThrust_input'].update(values['forceThrust_input'][:-1])

    if event == 'consumption_fuel_input':
      if values['consumption_fuel_input'][-1] not in ('0123456789'):
         psg.popup("Only digits allowed")
         window['consumption_fuel_input'].update(values['consumption_fuel_input'][:-1])

    if event == 'simulation_speed_input':
      if values['simulation_speed_input'][-1] not in ('0123456789'):
         psg.popup("Only digits allowed")
         window['simulation_speed_input'].update(values['simulation_speed_input'][:-1])
