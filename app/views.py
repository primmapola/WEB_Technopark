from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

questions = [
        {
            'id': i+1,
            'title': f'Question {i+1}',
            'content': f'Lorem ipsum? {i+1}'
        } for i in range(15)
    ]


def index(request):
    items_per_page = 3

    paginator = Paginator(questions, items_per_page)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})

def question(request, question_id):
    item = questions[question_id-1]
    return render(request, template_name='question.html', context={'question': item})

def ask(request):
    return render(request, template_name='ask.html')

from django.shortcuts import render

def tagged_questions(request, tag_name):
    items_per_page = 3

    paginator = Paginator(questions, items_per_page)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'tagged_questions.html', {'page_obj': page_obj, 'tag_name': tag_name})

def settings(request):
    return render(request, template_name='settings.html')

def login(request):
    return render(request, template_name='login.html', context={'error_message': True})

def signup(request):
    return render(request, template_name='signup.html', context={'error_message': True})