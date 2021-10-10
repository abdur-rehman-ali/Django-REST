from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from .models import student
from .serializer import studentSerializer

# Create your views here.

#Model object 
def studentAPI(request):
    #Model object data
    data = student.objects.get(id=2)
    print(data)
    #serializing data and converting it into python native datatypes
    serializer = studentSerializer(data)
    print(serializer)
    #python dictionery of data
    print(serializer.data)
    #json format of data
    # json = JSONRenderer().render(serializer.data)
    # print(json)
    # return HttpResponse(json, content_type="application/json")
    return JsonResponse(data=serializer.data)

#Return queryset     
def studentAPIList(request):
    #Model object data
    data = student.objects.all()
    print(data)
    #serializing data and converting it into python native datatypes
    serializer = studentSerializer(data,many=True)
    print(serializer)
    #python dictionery of data
    print(serializer.data)
    #json format of data
    # json = JSONRenderer().render(serializer.data)
    # print(json)
    # return HttpResponse(json, content_type="application/json")
    #Here we set safe = False because our data is not off dict type
    return JsonResponse(serializer.data,safe=False)