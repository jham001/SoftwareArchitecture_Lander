import sqlite3 #database library

#declare table name as a global variable
table_name = f""
#connect to blackboard using a global variable
dbConnection = sqlite3.connect('blackboard.db')
#connect cursor as a global variable
cursor = dbConnection.cursor() # Connect cursor as a global variable

#function to create new table in the database
def newTable(time_elapsed, h, v, m_fuel, m_lander, displacement, acceleration, impactTime):
    #declare that you are modifying the global variables within this function
    global table_name
    global dbConnection
    global cursor

    #execute a query to get the number of tables
    cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table';")

    #fetch the result
    num_tables = cursor.fetchone()[0]

    #print the number of tables
    print("Number of tables in the database:", num_tables)
    table_name = f"blackboard_display_data{num_tables}"
    print(table_name)

    #create a new table
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
    (
    time_elapsed_sec float PRIMARY KEY,
    altitude float,
    velocity float,
    fuel_mass float,
    lander_mass float,
    displacement float,
    acceleration float,
    time_till_impact float
    );''')

    #add Initial values
    Time = time_elapsed
    Altitude = h
    Velocity = v
    Fuel = m_fuel
    LanderMass = m_lander
    Displacement = displacement
    Acceleration = acceleration
    TTI = impactTime

    #construct the SQL command for insertion
    sqlCommand = f"INSERT INTO {table_name} (time_elapsed_sec, altitude, velocity, fuel_mass, lander_mass, displacement, acceleration, time_till_impact) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

    #execute the insertion with parameterized values
    cursor.execute(sqlCommand, (Time, Altitude, Velocity, Fuel, LanderMass, Displacement, Acceleration, TTI))

    #commit the changes
    dbConnection.commit()    

#getter function that returns altitude from database
def getAltitude():
    #declare that you are modifying the global variables within this function
    global table_name
    global dbConnection
    global cursor
    #value from last row, altitude column
    sqlCommand = f"SELECT altitude FROM {table_name} ORDER BY time_elapsed_sec DESC LIMIT 1"
    cursor = dbConnection.execute(sqlCommand)
    #initialize a result variable
    result = 0
    #store latest row in query result 
    row = cursor.fetchone()
    #if the row exists then store value of row 0 in the result variable 
    if row:
        result = row[0]
    #return result
    return result  

#getter function that returns velocity from database
def getVelocity():
    #declare that you are modifying the global variables within this function
    global table_name
    global dbConnection
    global cursor
    #value from last row, velocity column
    sqlCommand = f"select velocity from {table_name}"
    cursor = dbConnection.execute(sqlCommand)
    #initialize a result variable
    result = 0
    #store row 0 result in the result variable
    for row in cursor:
        result = row[0]
    #return row
    return result

#getter function that returns fuel mass from database
def getFuelMass():
    #declare that you are modifying the global variables within this function
    global table_name
    global dbConnection
    global cursor
    #value from last row, fuel mass column
    sqlCommand = f"select fuel_mass from {table_name}"
    cursor = dbConnection.execute(sqlCommand)
    #store row 0 result in the result variable
    result = 0
    for row in cursor:
        result =  row[0]
    #return row
    return result

#getter function that returns lander mass from database
def getLanderMass():
    #declare that you are modifying the global variables within this function
    global table_name
    global dbConnection
    global cursor
    #value from last row, lander mass column
    sqlCommand = f"select lander_mass from {table_name}"
    cursor = dbConnection.execute(sqlCommand)
    #store row 0 result in the result variable
    result = 0
    for row in cursor:
        result =  row[0]
    #return row
    return result   

#getter function that returns total mass from database
def getTotalMass():
    #declare that you are modifying the global variables within this function
    global table_name
    global dbConnection
    global cursor
    #value from last row, lander mass column
    sqlCommand = f"select total_mass from {table_name}"
    cursor = dbConnection.execute(sqlCommand)
    #store row 0 result in the result variable
    result = 0
    for row in cursor:
        result =  row[0]
    #return row
    return result

#function adds row to database using parameters converted into a SQL command
def addRow(time_elapsed, h, v, m_fuel, m_lander, displacement, acceleration, impactTime):
    #declare that you are modifying the global variables within this function
    global table_name
    global dbConnection
    global cursor

    #add new row to DB with this data
    Time = time_elapsed
    Altitude = h
    Velocity = v
    Fuel = m_fuel
    LanderMass = m_lander
    Displacement = displacement
    Acceleration = acceleration
    TTI = impactTime

    #construct the SQL command for insertion
    sqlCommand = f"INSERT INTO {table_name} (time_elapsed_sec, altitude, velocity, fuel_mass, lander_mass, displacement, acceleration, time_till_impact) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

    #execute the insertion with parameterized values
    cursor.execute(sqlCommand, (Time, Altitude, Velocity, Fuel, LanderMass, Displacement, Acceleration, TTI))
    dbConnection.commit()

#function closes the database connection and the cursor 
def close():
    #declare global variables
    global dbConnection
    global cursor
    #close both global variables
    cursor.close()
    dbConnection.close()