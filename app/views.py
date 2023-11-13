from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    questions = [
        {
            'id': index,
            'title': f'Question {index}',
            'content': f'Lorem ipsum? {index}'
        } for i in range(5)
    ]
    return render(request, template_name='index.html', context={'questions': questions})

def question(request):
    return render(request, template_name='question.html')
