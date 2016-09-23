from django.shortcuts import get_object_or_404, render
import requests
import json



def index(request):
    """ static index page """
    return render(request, 'index.html', {})


def questions_static(request):
    """ static questions page, using django's templating system """
    r = requests.get('http://127.0.0.1:8000/api/v1/questions/')
    print("questions: {}".format(r.text))
    context = {
        'questions': r.json()
    }
    return render(request, 'static_questions.html', context)
