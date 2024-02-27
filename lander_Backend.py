# libraries
import sqlite3

# Connect to blackboard
dbConnection = sqlite3.connect('blackboard.db')

# Create a cursor object
cursor = dbConnection.cursor()

# Execute a query to get the number of tables
cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table';")

# Fetch the result
num_tables = cursor.fetchone()[0]

# Print the number of tables
print("Number of tables in the database:", num_tables)
table_name = f"blackboard_display_data{num_tables - 1}"

# create a new table
cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
(
time_elapsed_sec numeric(12,4),
altitude numeric(12,4),
velocity numeric(12,4),
fuel_mass numeric(12,4),
lander_mass numeric(12,4),
displacement numeric(12,4)
);''')


# Add Initial values
Time = str(1)
Altitude = str(100000)
Velocity = str(1)
Fuel = str(1)
LanderMass = str(1)
Displacement = str(0)

# Construct the SQL command for insertion
sqlCommand = f"INSERT INTO {table_name} (time_elapsed_sec, altitude, velocity, fuel_mass, lander_mass, displacement) VALUES (?, ?, ?, ?, ?, ?)"

# Execute the insertion with parameterized values
cursor.execute(sqlCommand, (Time, Altitude, Velocity, Fuel, LanderMass, Displacement))

# Commit the changes
dbConnection.commit()







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
cursor.close()
dbConnection.close()
