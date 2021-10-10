from django.shortcuts import HttpResponse
import io
from rest_framework.parsers import JSONParser
from .serializer import studentSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def studentAPI(request):
    """
    This view will handle the post requests made by other applications for adding
    data to student model
    """
    if request.method == 'POST':
        #data will contain json
        data = request.body
        print(data)
        stream = io.BytesIO(data)
        print(stream)
        #Json data is converted to python data
        python_data = JSONParser().parse(stream)
        print(python_data)
        #Converting python data to complex data type(i.e. model instances)
        serializer = studentSerializer(data=python_data)
        print(serializer)
        if serializer.is_valid():
            #Save the data to database if it is valid
            serializer.save()
            #We have to send response of request made
            response_msg = {
                'message':'Your data has been added to database'
            }
            #Converting python object to json data
            json_data = JSONRenderer().render(response_msg)
            #returnng json response
            return HttpResponse(json_data, content_type="application/json")
        else:
            #If some error occur then return that error as response
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type="application/json")
