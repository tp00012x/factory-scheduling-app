from rest_framework import serializers

from ..models.space_vehicle_order import SpaceVehicleOrder


class SpaceVehicleOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SpaceVehicleOrder
        fields = ('pk', 'name',)
