# PlatziGram Views.

# Django
from django.http import HttpResponse
from datetime import datetime
import json

def helloWorld(request):
    return HttpResponse('Oh ,Hi!! current server time is {now}'.format(
        now= datetime.now().strftime('%b %dth , %Y - %H:%M hrs ')
        ))

def sortIntegger(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status':'ok',
        'numbers' : sorted_ints,
        'message' : 'integer sorted succesfully.'
    }
    return HttpResponse(json.dumps(data, indent= 4),content_type='application/json')

def sayHi(request, name, age):
    if age < 12:
        message = 'sorry {}, you are not allowed here'.format(name)

    else:
        message = 'Hello, {}!!, welcome to Platzgram'.format(name)

    return HttpResponse(message)