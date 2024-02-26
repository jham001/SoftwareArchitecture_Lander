# libraries
import sqlite3

# create a new table
dbConnection.execute('''create table blackboard_display_data
(
time_elapsed_sec numeric(12,4),
altitude numeric(12,4),
velocity numeric(12,4),
fuel_mass numeric(12,4),
lander_mass numeric(12,4),
total_mass numeric(12,4),
displacement numeric(12,4)
);''')

dbConnection.execute('''create table blackboard_constraints
(
landing_height numeric (3,2),
max_landing_velocity numeric(3,2)
);''')

def getAltitude():
    # Value from last row, altitude column
    sqlCommand = "select altitude from blackboard_display_data"
    cursor = dbConnection.execute(sqlCommand)
    for row in cursor:
        return row[0]

def getVelocity():
    # Value from last row, velocity column
    sqlCommand = "select velocity from blackboard_display_data"
    cursor = dbConnection.execute(sqlCommand)
    for row in cursor:
        return row[0]

def getFuelMass():
    # Value from last row, fuel mass column
    sqlCommand = "select fuel_mass from blackboard_display_data"
    cursor = dbConnection.execute(sqlCommand)
    for row in cursor:
        return row[0]

def getLanderMass():
    # Value from last row, lander mass column
    sqlCommand = "select lander_mass from blackboard_display_data"
    cursor = dbConnection.execute(sqlCommand)
    for row in cursor:
        return row[0]     

def getTotalMass():
    # Value from last row, total mass column
    sqlCommand = "select total_mass from blackboard_display_data"
    cursor = dbConnection.execute(sqlCommand)
    for row in cursor:
        return row[0]

def AddRow(time_elapsed, h, v, m_fuel, m_lander, m_total, displacement):
    # Add new row to DB with this data
    value1 = str(time_elapsed)
    value2 = str(h)
    value3 = str(v)
    value4 = str(m_fuel)
    value5 = str(m_lander)
    value6 = str(m_total)
    value7 = str(displacement)
    sqlCommand = "insert into blackboard_display_data values" + "(\"" + value1 + "\", \"" + value2 + "\", " + value3 + ", " + value4 + ", " + value5 + ", " + value6 + ", " + value7 + ")"
    dbConnection.execute(sqlCommand)
    dbConnection.commit()

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

