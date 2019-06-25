from rest_framework import serializers

from ..models.bill_of_material import BillOfMaterial


class BillOfMaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BillOfMaterial
        fields = ('pk', 'part_name', 'quantity', 'space_vehicle_order', 'work_center')
