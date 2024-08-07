from rest_framework import serializers
from .models import Sensor, Measurement

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['sensor_key', 'sensor_id', 'location']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'timestamp', 'temperature', 'humidity', 'timezone', 'temperature_change_rate', 'humidity_change_rate', 'comfort_index', 'comfort_level', 'sensor']
