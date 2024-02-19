# libraries
import sqlite3

# Connect to blackboard
DATA = sqlite3.connect('blackboard.db')
print("Connection established ..........")


DATA.execute ('''CREATE TABLE CRICKETERS (
   First_Name VARCHAR(255),
   Last_Name VARCHAR(255),
   Age int,
   Place_Of_Birth VARCHAR(255),
   Country VARCHAR(255)
);''')

# DB
    # Table Trial #1
    # Table Trial #2

# Make DB if it does not exist
# Get number of latest trial
# Make a new Table with new trial number
    # This is the Table we will use

# Table stores Altitude, Fuel, Weight, Velocity, Impact till Time, Displacement as columns
# Each row is a new timestamp
#   ex. t=0, t=1, t=2

# There should be a method to set them all
# There should be methods to get each individualy (Latest value for now)



# Close blackboard
DATA.close()

