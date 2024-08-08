#include <ESP8266WiFi.h>  // Include the ESP8266 WiFi library for WiFi connection
#include <ESP8266HTTPClient.h>  // Include the ESP8266 HTTP client library for HTTP requests
#include "DHT.h"  // Include the DHT sensor library for reading temperature and humidity data

#define DHTPIN 2  // Define the data pin for the DHT sensor as pin 2
#define DHTTYPE DHT22  // Define the DHT sensor type as DHT22

const char* ssid = "whyhd";  // Define the WiFi network SSID
const char* password = "eoeoeoeo";  // Define the WiFi network password
const String serverName = "http://10.82.1.156:5000";  // Define the server address (replace with your server IP address)

DHT dht(DHTPIN, DHTTYPE);  // Create a DHT sensor object, specifying the pin and sensor type

void setup() {
  Serial.begin(9600);  // Initialize serial communication with a baud rate of 9600
  WiFi.begin(ssid, password);  // Start connecting to the WiFi network

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);  // Delay for 1 second
    Serial.println("Connecting to WiFi...");  // Print the WiFi connection status
  }

  Serial.println("Connected to WiFi");  // Print the successful connection status
  dht.begin();  // Initialize the DHT sensor
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {  // Check if WiFi is connected
    WiFiClient client;  // Create a WiFi client object
    HTTPClient http;  // Create an HTTP client object
    float h = dht.readHumidity();  // Read humidity data
    float t = dht.readTemperature();  // Read temperature data

    if (isnan(h) || isnan(t)) {  // Check if the data read is valid
      Serial.println("Failed to read from DHT sensor!");  // Print the failed reading status
      return;  // Exit the function
    }

    // Create the request URL, including temperature and humidity data
    String url = serverName + "/update?sensor=dht22&temperature=" + String(t) + "&humidity=" + String(h);

    http.begin(client, url); // Initialize the HTTP request with the new begin method
    int httpCode = http.GET();  // Send the HTTP GET request

    if (httpCode > 0) {  // Check if the HTTP response code is greater than 0
      String payload = http.getString();  // Get the response content
      Serial.println("HTTP Response code: " + String(httpCode));  // Print the HTTP response code
      Serial.println("Response: " + payload);  // Print the response content
    } else {
      Serial.println("Error on HTTP request, HTTP Response code: " + String(httpCode));  // Print the HTTP request error
    }

    http.end();  // End the HTTP request
  } else {
    Serial.println("WiFi not connected");  // Print the WiFi not connected status
  }

  delay(2000);  // Delay for 2 seconds (adjust as needed)
}