from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import student
from .serializer import studentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def crudAPI(request):
    if request.method == 'GET':
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id is not None:
            data = student.objects.get(id=id)
            serializer = studentSerializer(data)
        else:
            data = student.objects.all()
            serializer = studentSerializer(data,many=True)
            print(serializer.data)
        json = JSONRenderer().render(serializer.data)
        return HttpResponse(json, content_type="application/json")


    if request.method == 'POST':
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        serializer = studentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response_msg={
                'msg':'Your data has been added to database'
            }
            json = JSONRenderer().render(response_msg)
            return HttpResponse(json, content_type="application/json")
        else:
            json = JSONRenderer().render(serializer.errors)
            return HttpResponse(json, content_type="application/json")


    if request.method == 'PUT':
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        id =  python_data.get('id')
        if id is not None:
            data_to_update = student.objects.get(id=id)
            serializer = studentSerializer(data_to_update,data=python_data,partial=True)
            if serializer.is_valid():
                serializer.save()
                response_msg={
                    'msg':'Your data has been updated in database'
                }
                json = JSONRenderer().render(response_msg)
                return HttpResponse(json, content_type="application/json")
            else:
                json = JSONRenderer().render(serializer.errors)
                return HttpResponse(json, content_type="application/json")
        else:
            response_msg={
                    'msg':'Your have not added id'
                }
            json = JSONRenderer().render(response_msg)
            return HttpResponse(json, content_type="application/json")

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id is not None:
            data = student.objects.get(id=id)
            data.delete()
            response={
                'msg':'data deleted',
            }
            return JsonResponse(response)
        else:
            response={
                'msg':'id is requited to delete the data',
            }
            return JsonResponse(response)
