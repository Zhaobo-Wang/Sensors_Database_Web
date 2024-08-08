import pandas as pd
import mysql.connector
import numpy as np

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123Wjb456+',
    database='sensor_data'
)

cursor = connection.cursor() # Create a cursor object to execute SQL statements

file_path = 'C:/Users/Frank/Desktop/New_DHT11_Data_Collection.xlsx' # Read data from the Excel file
sensors = pd.read_excel(file_path, sheet_name='Sensors') # Read the 'Sensors' sheet
measurements = pd.read_excel(file_path, sheet_name='Measurements') # Read the 'Measurements' sheet

# Remove duplicate primary key records
sensors = sensors.drop_duplicates(subset=['Sensor Key'])
measurements = measurements.drop_duplicates(subset=['ID'])

try:
    for index, row in sensors.iterrows(): # Iterate through each row of the Sensors DataFrame and insert data into the Sensors table, ignoring duplicate primary keys
        sql = "INSERT IGNORE INTO Sensors (Sensor_ID, Location, Sensor_Key) VALUES (%s, %s, %s)" # Define the insert statement, using INSERT IGNORE to avoid duplicate primary key errors
        params = (row['Sensor ID'], row['Location'], row['Sensor Key']) # Extract data from the current row
        print(f"Executing SQL: {sql} with params {params}") # Print the SQL statement and parameters to be executed for debugging purposes
        cursor.execute(sql, params) # Execute the insert operation

    for index, row in measurements.iterrows(): # Insert data into the Measurements table, ignoring duplicate primary keys
        sql = """INSERT IGNORE INTO Measurements (ID, Temperature, Humidity, Timestamp, TimeZone, Temperature_Change_Rate, 
                   Humidity_Change_Rate, Comfort_Index, Location, Sensor_ID, Comfort_Level) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" # Define the insert statement, using INSERT IGNORE to avoid duplicate primary key errors
        
        params = (row['ID'], row['Temperature'], row['Humidity'], row['Timestamp'], row['TimeZone'], 
                  row['Temperature Change Rate'], row['Humidity Change Rate'], row['Comfort Index'], row['Location'], row['Sensor ID'], row['Comfort Level']) # Extract data from the current row
        print(f"Executing SQL: {sql} with params {params}") # Print the SQL statement and parameters to be executed for debugging purposes
        cursor.execute(sql, params) # Execute the insert operation

    connection.commit() # Commit changes to the database to ensure all insert operations are saved

except mysql.connector.Error as err: # Catch and print database operation errors
    print("Error: {}".format(err))

finally: 
    cursor.close() # Close the cursor
    connection.close() # Close the connection