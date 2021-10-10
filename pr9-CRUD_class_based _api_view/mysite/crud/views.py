from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import  student
from .serializer import studentSerializer


class crudAPI(APIView):

    def get(self, request,pk=None, *args, **kwargs):
        id =pk
        if id is not None:
            data = student.objects.get(id=id)
            serializer = studentSerializer(data)
        else:
            data = student.objects.all()
            serializer = studentSerializer(data,many=True)
        return Response(data=serializer.data)


    def post(self, request, *args, **kwargs):

        python_data=request.data
        serializer = studentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response_msg={
                'msg':'Your data has been added to database'
            }
        
            return Response(data=response_msg)
        else:
            return Response(data=serializer.errors)

    def put(self, request,pk=None, *args, **kwargs):
        id =pk
        if id is not None:
            data_to_update = student.objects.get(id=id)
            serializer = studentSerializer(data_to_update,data=request.data)
            if serializer.is_valid():
                serializer.save()
                response_msg={
                    'msg':'Your data has been updated in database'
                }
                return Response(data=response_msg)
            else:
                return Response(data=serializer.errors)
        else:
            response_msg={
                    'msg':'You have not added id'
                }
            return Response(data=response_msg)

    def patch(self, request,pk=None, *args, **kwargs):
        id = pk
        if id is not None:
            data_to_update = student.objects.get(id=id)
            serializer = studentSerializer(data_to_update,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                response_msg={
                    'msg':'Your data has been partially updated in database'
                }
                return Response(data=response_msg)
            else:
                return Response(data=serializer.errors)
        else:
            response_msg={
                    'msg':'You have not added id'
                }
            return Response(data=response_msg)

    def delete(self, request,pk=None, *args, **kwargs):
        id =pk
        if id is not None:
            data = student.objects.get(id=id)
            data.delete()
            response={
                'msg':'data deleted',
            }
            return Response(data=response)
        else:
            response={
                'msg':'id is required to delete the data',
            }
            return Response(data=response)



