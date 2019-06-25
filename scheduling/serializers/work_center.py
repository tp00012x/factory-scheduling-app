from ..models.work_center import WorkCenter
from rest_framework import serializers


class WorkCenterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkCenter
        fields = ('pk', 'name',)
