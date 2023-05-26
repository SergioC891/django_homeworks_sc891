from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorViewSet(viewsets.ViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def list(self, request):
        serializer = SensorSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        sensor = get_object_or_404(self.queryset, pk=pk)
        serializer = SensorDetailSerializer(sensor)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        sensor = get_object_or_404(self.queryset, pk=pk)
        serializer = SensorSerializer(sensor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeasurementViewSet(viewsets.ViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def create(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
