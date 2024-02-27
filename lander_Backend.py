# libraries
import sqlite3

table_name = ""  # Declare table_name as a global variable

def newTable():
    global table_name  # Declare that you are modifying the global variable within this function

    # Connect to blackboard
    dbConnection = sqlite3.connect('blackboard.db')
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
    time_elapsed_sec float PRIMARY KEY,
    altitude float,
    velocity float,
    fuel_mass float,
    lander_mass float,
    displacement float
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
    
    # Close blackboard
    cursor.close()
    dbConnection.close()




def getAltitude():
    global table_name

    # Connect to blackboard
    dbConnection = sqlite3.connect('blackboard.db')
    cursor = dbConnection.cursor()

    # Value from last row, altitude column
    sqlCommand = f"SELECT altitude FROM {table_name} ORDER BY time_elapsed_sec DESC LIMIT 1"
    cursor = dbConnection.execute(sqlCommand)
    
    result = 0
    row = cursor.fetchone()
    if row:
        result = row[0]

    # Close blackboard
    cursor.close()
    dbConnection.close()
    
    print(f"Altitude: {result}")
    return result
    

def getVelocity():
    global table_name

    # Connect to blackboard
    dbConnection = sqlite3.connect('blackboard.db')
    cursor = dbConnection.cursor()

    # Value from last row, velocity column
    sqlCommand = f"select velocity from {table_name}"
    cursor = dbConnection.execute(sqlCommand)
    
    result = 0
    for row in cursor:
        result =  row[0]

    # Close blackboard
    cursor.close()
    dbConnection.close()
    
    print(f"Velocity: {result}")
    return result

def getFuelMass():
    global table_name

    # Connect to blackboard
    dbConnection = sqlite3.connect('blackboard.db')
    cursor = dbConnection.cursor()

    # Value from last row, fuel mass column
    sqlCommand = f"select fuel_mass from {table_name}"
    cursor = dbConnection.execute(sqlCommand)
    
    result = 0
    for row in cursor:
        result =  row[0]

    # Close blackboard
    cursor.close()
    dbConnection.close()
    
    print(f"FuelMass: {result}")
    return result

def getLanderMass():
    global table_name

    # Connect to blackboard
    dbConnection = sqlite3.connect('blackboard.db')
    cursor = dbConnection.cursor()

    # Value from last row, lander mass column
    sqlCommand = f"select lander_mass from {table_name}"
    cursor = dbConnection.execute(sqlCommand)
    
    result = 0
    for row in cursor:
        result =  row[0]

    # Close blackboard
    cursor.close()
    dbConnection.close()
    
    print(f"LanderMass: {result}")
    return result   

def getTotalMass():
    global table_name

    # Connect to blackboard
    dbConnection = sqlite3.connect('blackboard.db')
    cursor = dbConnection.cursor()

    # Value from last row, total mass column
    sqlCommand = f"select total_mass from {table_name}"
    cursor = dbConnection.execute(sqlCommand)
    
    result = 0
    for row in cursor:
        result =  row[0]

    # Close blackboard
    cursor.close()
    dbConnection.close()
    
    print(f"TotalMass: {result}")
    return result

def AddRow(time_elapsed, h, v, m_fuel, m_lander, m_total, displacement):
    global table_name

    # Connect to blackboard
    dbConnection = sqlite3.connect('blackboard.db')

    # Add new row to DB with this data
    value1 = str(time_elapsed)
    value2 = str(h)
    value3 = str(v)
    value4 = str(m_fuel)
    value5 = str(m_lander)
    value6 = str(m_total)
    value7 = str(displacement)
    sqlCommand = f"insert into {table_name} values" + "(\"" + value1 + "\", \"" + value2 + "\", " + value3 + ", " + value4 + ", " + value5 + ", " + value6 + ", " + value7 + ")"
    dbConnection.execute(sqlCommand)
    dbConnection.commit()
    
    # Close blackboard
    dbConnection.close()


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
  
