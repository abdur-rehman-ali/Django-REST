from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import student
from .serializer import studentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response 

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def crudAPI(request,pk=None):
    if request.method == 'GET':
        id =pk
        if id is not None:
            data = student.objects.get(id=id)
            serializer = studentSerializer(data)
        else:
            data = student.objects.all()
            serializer = studentSerializer(data,many=True)
        return Response(data=serializer.data)


    if request.method == 'POST':
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


    if request.method == "PATCH":
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
                    'msg':'Your have not added id'
                }
            return Response(data=response_msg)

    if request.method == 'PUT':
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
                    'msg':'Your have not added id'
                }
            return Response(data=response_msg)

    if request.method == 'DELETE':
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
                'msg':'id is requited to delete the data',
            }
            return Response(data=response)
