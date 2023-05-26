from django.urls import path, include
from rest_framework import routers

from .views import SensorViewSet, MeasurementViewSet

router = routers.DefaultRouter()
router.register(r'sensors', SensorViewSet)
router.register(r'measurements', MeasurementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
