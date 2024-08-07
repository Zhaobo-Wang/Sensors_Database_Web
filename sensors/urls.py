from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SensorViewSet, MeasurementViewSet, index

router = DefaultRouter()
router.register(r'sensors', SensorViewSet)
router.register(r'measurements', MeasurementViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
    path('api/sensors/search/', SensorViewSet.as_view({'get': 'search'}), name='sensor-search'),
    path('api/measurements/search/', MeasurementViewSet.as_view({'get': 'search'}), name='measurement-search'),
]
