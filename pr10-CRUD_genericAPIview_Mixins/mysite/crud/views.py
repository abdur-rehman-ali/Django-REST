from rest_framework.views import APIView
from rest_framework.response import Response
from .models import student
from .serializer import studentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

#This class dont require id
class crudAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = student.objects.all()
    serializer_class = studentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

#This class require id
class crudAPIViewWithId(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = student.objects.all()
    serializer_class = studentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args,**kwargs)
