from django.shortcuts import render
from enrolment.models import student
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def enroll(request):
    if request.method == 'POST':
        body = request.body
        content = json.loads(body)
        stud = student(first_name=content['first_name'],last_name=content['last_name'])
        stud.save()
        return HttpResponse(status=200)
    elif request.method == 'GET':
        #leggiamo da db e ritorniamo al client
        stud = student.objects.all()
        list_student = [{'first_name':s.first_name,'last_name':s.last_name}for s in stud]
        resp = json.dumps(list_student)
        return HttpResponse(resp, content_type='application/json')