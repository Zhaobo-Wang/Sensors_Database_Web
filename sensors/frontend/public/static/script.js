console.log('JavaScript file loaded'); 

let myChart = null;

async function fetchSensors() {
    try {
        const response = await fetch('/api/sensors/');
        const sensors = await response.json();
        console.log('Sensors:', sensors); 
        const sensorsList = document.getElementById('sensors-list');
        sensorsList.innerHTML = '';
        sensors.forEach(sensor => {
            const listItem = document.createElement('li');
            listItem.textContent = `${sensor.sensor_id} - ${sensor.location}`;
            sensorsList.appendChild(listItem);
        });
    } catch (error) {
        console.error('Error fetching sensors:', error);
    }
}

async function fetchMeasurements() {
    try {
        const response = await fetch('/api/measurements/');
        const measurements = await response.json();
        console.log('Measurements:', measurements); 
        const measurementsList = document.getElementById('measurements-list');
        measurementsList.innerHTML = '';
        measurements.forEach(measurement => {
            const listItem = document.createElement('li');
            listItem.textContent = `Sensor ID: ${measurement.id} - ${measurement.temperature}°C - ${measurement.humidity}%`;
            measurementsList.appendChild(listItem);
        });
    } catch (error) {
        console.error('Error fetching measurements:', error);
    }
}

async function searchSensors() {
    const query = document.getElementById('query').value;
    try {
        const response = await fetch(`/api/sensors/search/?query=${query}`);
        const sensors = await response.json();
        console.log('Search Sensors:', sensors); 
        const sensorsList = document.getElementById('sensors-list');
        sensorsList.innerHTML = '';
        sensors.forEach(sensor => {
            const listItem = document.createElement('li');
            listItem.textContent = `${sensor.sensor_id} - ${sensor.location}`;
            sensorsList.appendChild(listItem);
        });
    } catch (error) {
        console.error('Error searching sensors:', error);
    }
}

async function searchMeasurements() {
    const query = document.getElementById('query').value;
    try {
        const response = await fetch(`/api/measurements/search/?query=${query}`);
        const measurements = await response.json();
        console.log('Search Measurements:', measurements); 
        const measurementsList = document.getElementById('measurements-list');
        measurementsList.innerHTML = '';
        measurements.forEach(measurement => {
            const listItem = document.createElement('li');
            listItem.textContent = `Sensor ID: ${measurement.id} - ${measurement.temperature}°C - ${measurement.humidity}%`;
            measurementsList.appendChild(listItem);
        });
    } catch (error) {
        console.error('Error searching measurements:', error);
    }
}


async function showChart() {
    try {
        const response = await fetch('/api/measurements/');
        const measurements = await response.json();
        console.log('Measurements for chart:', measurements);
        const timestamps = measurements.map(m => m.timestamp);
        const temperatures = measurements.map(m => m.temperature);
        const humidities = measurements.map(m => m.humidity);

        const ctx = document.getElementById('myChart').getContext('2d');

        if (myChart) {
            myChart.destroy();
        }

        myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: timestamps,
                datasets: [
                    {
                        label: 'Temperature (°C)',
                        data: temperatures,
                        borderColor: 'rgba(255, 99, 132, 1)',
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        fill: false,
                    },
                    {
                        label: 'Humidity (%)',
                        data: humidities,
                        borderColor: 'rgba(54, 162, 235, 1)',
                        backgroundColor: 'rgba(54, 162, 235, 0.2)',
                        fill: false,
                    }
                ]
            },
            options: {
                responsive: true,
                scales: {
                    x: {
                        type: 'time',
                        time: {
                            unit: 'minute'
                        }
                    },
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });

        document.getElementById('myChart').style.display = 'block';
    } catch (error) {
        console.error('Error fetching measurements for chart:', error);
    }
}