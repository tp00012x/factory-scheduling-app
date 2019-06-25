from ..models.bill_of_material import BillOfMaterial
from ..serializers.bill_of_material import BillOfMaterialSerializer
from rest_framework import viewsets


class BillOfMaterialViewSet(viewsets.ModelViewSet):
    queryset = BillOfMaterial.objects.all()
    serializer_class = BillOfMaterialSerializer
