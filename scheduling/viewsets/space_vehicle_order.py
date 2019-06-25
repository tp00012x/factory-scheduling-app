from rest_framework import viewsets

from scheduling.models.space_vehicle_order import SpaceVehicleOrder
from scheduling.serializers.space_vehicle_order import SpaceVehicleOrderSerializer


class SpaceVehicleOrderViewSet(viewsets.ModelViewSet):
    queryset = SpaceVehicleOrder.objects.all()
    serializer_class = SpaceVehicleOrderSerializer
