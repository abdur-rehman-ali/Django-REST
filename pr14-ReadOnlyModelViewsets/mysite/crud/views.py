from .models import student
from .serializer import studentSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response


class studentViewset(ReadOnlyModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer
        