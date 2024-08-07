from django.db import models

class Sensor(models.Model):
    sensor_key = models.CharField(max_length=50, primary_key=True)
    sensor_id = models.CharField(max_length=50, default='DEFAULT_ID')
    location = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'sensors'

class Measurement(models.Model):
    id = models.IntegerField(primary_key=True)
    timestamp = models.DateTimeField()
    temperature = models.FloatField(default=0.0)
    humidity = models.IntegerField(default=0)
    timezone = models.CharField(max_length=50, default='Unknown')
    temperature_change_rate = models.CharField(max_length=50, null=True, blank=True)
    humidity_change_rate = models.CharField(max_length=50, null=True, blank=True)
    comfort_index = models.FloatField(default=0.0)
    comfort_level = models.CharField(max_length=50, default='Unknown')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, default=1)  # 外键字段名称

    class Meta:
        db_table = 'measurements'
