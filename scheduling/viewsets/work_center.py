from rest_framework import viewsets

from scheduling.models.work_center import WorkCenter
from scheduling.serializers.work_center import WorkCenterSerializer


class WorkCenterViewSet(viewsets.ModelViewSet):
    queryset = WorkCenter.objects.all()
    serializer_class = WorkCenterSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        print(request.method)
        print(request.stream)

        return super(WorkCenterViewSet, self).create(request, *args, **kwargs)
