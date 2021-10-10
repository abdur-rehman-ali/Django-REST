
from .models import student
from .serializer import studentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# This class dont require id
class crudAPI(ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer


#This class require id
class crudAPIViewWithId(RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer

