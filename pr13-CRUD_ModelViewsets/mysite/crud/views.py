from .models import student
from .serializer import studentSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response


class studentViewset(ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer
        