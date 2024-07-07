from django.shortcuts import render
from django.http import JsonResponse
from myfirstapp.models import Course
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def apiCourse(request):
    if (request.method == "GET"):
        # Serialize the data into json        
        data = serializers.serialize("json", Course.objects.all())
        # Turn the JSON data into a dict and send as JSON response             
        return JsonResponse(json.loads(data), safe=False)

    if (request.method == "POST"):
        # Turn the body into a dict        
        body = json.loads(request.body.decode("utf-8"))
        # filter data        
        if not body:
                data = '{"message": "data is not json type!"}'            
                dumps = json.loads(data)
                return JsonResponse(dumps, safe=False)
        else:
            created = Course.objects.create(
                course_name=body['course_name']
            )
            data = '{"message": "data successfully created!"}'            
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)

    if request.method == "PUT":
        body = json.loads(request.body.decode("utf-8"))
        if not body:
            data = '{"message": "data is not json type!"}'
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)
        else:
            try:
                course = Course.objects.get(id=body['id'])
                course.course_name = body['course_name']
                course.save()
                data = '{"message": "data successfully updated!"}'
                dumps = json.loads(data)
                return JsonResponse(dumps, safe=False)
            except Course.DoesNotExist:
                return HttpResponseNotFound('Course not found')

    if request.method == "DELETE":
        body = json.loads(request.body.decode("utf-8"))
        if not body or 'id' not in body:
            data = '{"message": "Invalid request"}'
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)
        else:
            try:
                course = Course.objects.get(id=body['id'])
                course.delete()
                data = '{"message": "data successfully deleted!"}'
                dumps = json.loads(data)
                return JsonResponse(dumps, safe=False)
            except Course.DoesNotExist:
                return HttpResponseNotFound('Course not found')

    return HttpResponseBadRequest('Invalid HTTP method')

