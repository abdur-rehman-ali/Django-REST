from .models import student
from .serializer import studentSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class studentViewset(ViewSet):

    def list(self,request):
        """
        This method wil display all the data in database
        """
        data = student.objects.all()
        serializer = studentSerializer(data, many=True)
        return Response(data=serializer.data)

    

    def create(self, request):
        """
        This method wil add  data in database
        """
        serializer = studentSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'msg':'Your data has been added to database'})
        else:
            return Response(data=serializer.errors)

    def retrieve(self, request, pk=None):
        """
        This method wil get single data from database
        """
        data = student.objects.get(id=pk)
        serializer = studentSerializer(data)
        return Response(data=serializer.data)


    def update(self, request, pk=None):
        """
        This method wil update data in database
        """
        data_to_update = student.objects.get(id=pk)
        serializer = studentSerializer(data_to_update,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'msg':'Your data has been updated'})
        else:
            return Response(data=serializer.errors)

    def partial_update(self, request, pk=None):
        """
        This method wil partially update data in database
        """
        data_to_update = student.objects.get(id=pk)
        serializer = studentSerializer(data_to_update,request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'msg':'Your data has been partially updated'})
        else:
            return Response(data=serializer.errors)

    def destroy(self, request, pk=None):
        """
        This method wil delete data in database
        """
        data = student.objects.get(id=pk)
        data.delete()
        response = {
                'msg': 'data deleted',
            }
        return Response(data=response)