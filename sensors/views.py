from rest_framework import viewsets
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('query', None)
        if query:
            sensors = self.queryset.filter(sensor_id__icontains=query)  # Assuming 'name' is a field in the Sensor model
            serializer = self.get_serializer(sensors, many=True)
            return Response(serializer.data)
        return Response([])

class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('query', None)
        if query:
            measurements = self.queryset.filter(timezone__icontains=query)  # Assuming 'sensor_id' is a foreign key with a 'name' field in the Measurement model
            serializer = self.get_serializer(measurements, many=True)
            return Response(serializer.data)
        return Response([])

def index(request):
    return render(request, 'frontend/public/index.html')
