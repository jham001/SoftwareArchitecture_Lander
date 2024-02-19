# libraries
import sqlite3


def getAltitude():
    # Value from last row, Altitude Column
    return 1 

def getVelocity():
    # Value from last row, Velocity Column
    return 1 

def getMass():
    # Value from last row, Velocity Column
    return 1     

def getFuel():
    # Value from last row, Velocity Column
    return 1 

# Connect to blackboard
DATA = sqlite3.connect('blackboard.db')
print("Connection established ..........")




# DB
    # Table Trial #1
    # Table Trial #2

# Make DB if it does not exist
# Get number of latest trial
# Make a new Table with new trial number
    # This is the Table we will use

# Table stores Altitude, Fuel, Weight, Velocity, Time till Impact, Displacement as columns
# Each row is a new timestamp
#   ex. t=0, t=1, t=2

    # New Table will hold initial values, Dont worry about them too much for now, can use placeholders.
    # Altitude = 100000, Fuel = placeholder, Weight = placeholder, Velocity = placeholder, Time till Impact = 1, Displacement = 0



# There should be a method to set them all
# There should be methods to get each individualy (Latest value for now)
  


# Close blackboard
DATA.close()

