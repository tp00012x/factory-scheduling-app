from django.db import models

from .space_vehicle_order import SpaceVehicleOrder
from .work_center import WorkCenter


class BillOfMaterial(models.Model):
    part_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    space_vehicle_order = models.ForeignKey(SpaceVehicleOrder, on_delete=models.CASCADE)
    work_center = models.ForeignKey(WorkCenter, on_delete=models.CASCADE)

    def __str__(self):
        return self.part_name

