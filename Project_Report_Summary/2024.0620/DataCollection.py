import serial  # For serial communication
import pandas as pd  # For data processing
import time  # For timestamps and loop delay

# Open serial communication on COM8 with a baud rate of 9600
ser = serial.Serial('COM8', 9600)

# Initialize a dictionary to store timestamps, humidity, and temperature data
data = {'Timestamp': [], 'Humidity': [], 'Temperature': []}

try:
    while True:
        line = ser.readline().decode('utf-8').strip()  # Read serial data
        # ser.readline() reads a line of data, decode('utf-8') decodes it to a UTF-8 string, strip() removes whitespace

        if "Humidity" in line and "Temperature" in line:  # Check if line contains "Humidity" and "Temperature"
            parts = line.split('\t')
            humidity = parts[0].split(': ')[1].split(' ')[0]  # Extract humidity value
            temperature = parts[1].split(': ')[1].split(' ')[0]  # Extract temperature value

            # Add timestamp, humidity, and temperature data to dictionary
            data['Timestamp'].append(time.strftime("%Y-%m-%d %H:%M:%S"))
            data['Humidity'].append(humidity)
            data['Temperature'].append(temperature)

            print(f'Time: {data["Timestamp"][-1]}, Humidity: {humidity}, Temperature: {temperature}')

            # Save data to Excel file every 10 entries
            if len(data['Timestamp']) % 10 == 0:
                df = pd.DataFrame(data)  # Convert dictionary to DataFrame
                df.to_excel('sensor_data.xlsx', index=False)  # Save DataFrame to Excel file without index
                print('Data saved to Excel')

        time.sleep(2)  # Pause for 2 seconds to control data reading frequency

# Save data to Excel file and close serial port on program exit
except KeyboardInterrupt:
    df = pd.DataFrame(data) 
    df.to_excel('sensor_data.xlsx', index=False)
    ser.close()
    print('Data saved to Excel and serial port closed')