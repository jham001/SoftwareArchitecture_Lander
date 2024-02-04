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

# Close blackboard
DATA.close()

