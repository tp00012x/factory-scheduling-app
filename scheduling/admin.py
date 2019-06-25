from django.contrib import admin
from .models.bill_of_material import BillOfMaterial
from .models.space_vehicle_order import SpaceVehicleOrder
from .models.work_center import WorkCenter


admin.site.register(BillOfMaterial)
admin.site.register(SpaceVehicleOrder)
admin.site.register(WorkCenter)

