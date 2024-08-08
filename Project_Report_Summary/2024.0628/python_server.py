from flask import Flask, request  # Import Flask and request modules to create a server and handle requests
import pandas as pd  # Import pandas module for data processing and saving to Excel
import time  # Import time module for delay operations in the thread
from threading import Thread  # Import Thread module to create an independent thread
from datetime import datetime, timedelta  # Import datetime module to get the current time

app = Flask(__name__)  # Create a Flask application instance

# Initialize a dictionary to store timestamps, humidity, and temperature data
data = {'Timestamp': [], 'Humidity': [], 'Temperature': []}

def save_data_to_excel():
    while True:
        time.sleep(20)  # Save data every 20 seconds
        if data['Timestamp']:  # If there is data
            df = pd.DataFrame(data)  # Convert the dictionary to a pandas DataFrame
            df.to_excel('sensor_data.xlsx', index=False)  # Save the DataFrame to an Excel file without saving the index
            print('Data saved to Excel')  # Print a message indicating the data was saved successfully

@app.route('/update', methods=['GET'])  # Define a route and handler method to process GET requests
def update():
    sensor = request.args.get('sensor')  # Get the sensor type from the request
    temperature = request.args.get('temperature')  # Get the temperature data from the request
    humidity = request.args.get('humidity')  # Get the humidity data from the request
    
    # Add the timestamp, humidity, and temperature data to the dictionary
    data['Timestamp'].append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  # Add the current timestamp
    data['Humidity'].append(humidity)  # Add the humidity data
    data['Temperature'].append(temperature)  # Add the temperature data
    
    print(f"Received data: Sensor={sensor}, Temperature={temperature}, Humidity={humidity}")  # Print the received data
    return "Data received"  # Return a response message

if __name__ == '__main__':  # Start a thread to periodically save data to the Excel file
    save_thread = Thread(target=save_data_to_excel)  # Create a thread with the target function save_data_to_excel
    save_thread.start()  # Start the thread
    app.run(host='0.0.0.0', port=5000)  # Start the Flask server, listening on all IP addresses at port 5000