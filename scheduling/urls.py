from django.conf.urls import url, include
from rest_framework import routers

from .viewsets.space_vehicle_order import SpaceVehicleOrderViewSet
from .viewsets.bill_of_material import BillOfMaterialViewSet
from .viewsets.work_center import WorkCenterViewSet


router = routers.DefaultRouter()
router.register(r'space_vehicle_orders', SpaceVehicleOrderViewSet)
router.register(r'bill_of_materials', BillOfMaterialViewSet)
router.register(r'work_centers', WorkCenterViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
