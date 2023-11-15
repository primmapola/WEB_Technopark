from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.models import Question, Tag, Answer

questions = [
        {
            'id': i+1,
            'title': f'Question {i+1}',
            'content': f'Lorem ipsum? {i+1}'
        } for i in range(15)
    ]


def paginate_items(request, items, items_per_page):
    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return page_obj

def index(request):
    items_per_page = 3
    page_obj = paginate_items(request, questions, items_per_page)

    return render(request, 'index.html', {'page_obj': page_obj})

def question(request, question_id):
    item = questions[question_id-1]
    return render(request, template_name='question.html', context={'question': item})

def ask(request):
    return render(request, template_name='ask.html')

def tagged_questions(request, tag_name):
    items_per_page = 3
    page_obj = paginate_items(request, questions, items_per_page)

    return render(request, 'tagged_questions.html', {'page_obj': page_obj})

def settings(request):
    return render(request, template_name='settings.html')

def login(request):
    return render(request, template_name='login.html', context={'error_message': True})

def signup(request):
    return render(request, template_name='signup.html', context={'error_message': True})

def hot(request):
    items_per_page = 3
    page_obj = paginate_items(request, questions, items_per_page)

    return render(request, 'hot.html', {'page_obj': page_obj})


