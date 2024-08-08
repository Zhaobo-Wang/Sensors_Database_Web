import pandas as pd

file_path = 'C:/Users/Frank/Desktop/Updated_DHT11_Data_Collection_v1.xlsx' # Define the path of the Excel file
xls = pd.ExcelFile(file_path) # Load the Excel file into Pandas' ExcelFile object

sheet_names = xls.sheet_names # Get the sheet names in the Excel file

df = pd.read_excel(file_path, sheet_name='Sheet1') # Load the first sheet of the Excel file into a DataFrame

df['Timestamp'] = pd.to_datetime(df['Timestamp']) # Convert the 'Timestamp' column to datetime format

# Create the sensors table

sensors = df[['Sensor ID','Location']].drop_duplicates().reset_index(drop=True)

sensors['Sensor ID'] = sensors['Sensor ID'].astype(str)
sensors['Location'] = sensors['Location'].astype(str)
sensors['Sensor Key'] = sensors.index + 1

# Create the Measurements table

measurements = df.drop(columns=['Location']).copy()
measurements = measurements.merge(sensors, on='Sensor ID', how='left')
measurements = measurements.drop(columns=['Sensor ID'])
measurements = measurements.rename(columns={'Sensor Key':'Sensor ID'})

# Group by 'TimeZone' and calculate the mean and standard deviation of 'Temperature' and 'Humidity'

grouped = measurements.groupby('TimeZone').agg({
    'Temperature': ['mean', 'std'],
    'Humidity': ['mean', 'std']
}).reset_index()

# Flatten the MultiIndex columns and rename them for easier understanding
grouped.columns = ['TimeZone', 'Mean Temperature', 'Temperature Std Dev', 
                   'Mean Humidity', 'Humidity Std Dev']

# Calculate the change rate of 'Temperature' and 'Humidity' and convert to percentage
measurements['Temperature Change Rate'] = measurements['Temperature'].pct_change() * 100
measurements['Humidity Change Rate'] = measurements['Humidity'].pct_change() * 100

# Calculate the comfort index with the formula: Temperature - Humidity * 0.55 + (Temperature - mean Temperature) * 0.1
measurements['Comfort Index'] = measurements['Temperature'] - measurements['Humidity'] * 0.55 + (measurements['Temperature'] - measurements['Temperature'].mean())*0.1

# Replace 0 values in temperature change rate with 'no change'
measurements['Temperature Change Rate'] = measurements['Temperature Change Rate'].apply(
    lambda x: 'no change' if x == 0 else x
)

# Replace 0 values in humidity change rate with 'no change'
measurements['Humidity Change Rate'] = measurements['Humidity Change Rate'].apply(
    lambda x: 'no change' if x == 0 else x
)

measurements['Comfort Level'] = pd.cut(measurements['Comfort Index'], bins=[-float('inf'), 
                                                                            measurements['Comfort Index'].quantile(0.33), 
                                                                            measurements['Comfort Index'].quantile(0.66), float('inf')], 
                                                                            labels=['Low', 'Medium', 'High'])

output_file_path_final = 'C:/Users/Frank/Desktop/New_DHT11_Data_Collection.xlsx'
with pd.ExcelWriter(output_file_path_final) as writer:
    sensors.to_excel(writer, sheet_name='Sensors', index=False)  # Save Sensors table
    measurements.to_excel(writer, sheet_name='Measurements', index=False)  # Save Measurements table
    grouped.to_excel(writer, sheet_name='Statistics', index=False)  # Save Statistics table

print(f"Data has been saved to {output_file_path_final}")  # Output the success message
print(f"Data has been saved to {output_file_path_final}") # Print the path of the saved file