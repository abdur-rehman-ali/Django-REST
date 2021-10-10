
from django.http import JsonResponse
from .models import student
from .serializer import studentSerializer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

#without api view
@csrf_exempt
def crudAPI(request):
    if request.method == 'GET':
        data = student.objects.all()
        serializer = studentSerializer(data,many=True)
        return JsonResponse(data=serializer.data,safe = False)
    
    if request.method == 'POST':
        #below three lines are used to convert json data into python data
        #but with api_view we can directly acceess python data using
        #requet.data
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)

        serializer = studentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'msg':'Data added to database'
            }
            return JsonResponse(data=response)
        else:
            return JsonResponse(serializer.errors)

 
# With api_view
@api_view(['GET','POST'])
def crudAPI(request):
    if request.method == 'GET':
        data = student.objects.all()
        serializer = studentSerializer(data,many=True)
        return Response(data=serializer.data)
    
    if request.method == 'POST':
        python_data = request.data
        serializer = studentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data added')
        else:
            return Response(serializer.errors)

