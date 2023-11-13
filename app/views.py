from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

questions = [
        {
            'id': i,
            'title': f'Question {i}',
            'content': f'Lorem ipsum? {i}'
        } for i in range(15)
    ]



# Assuming 'questions' is defined as before

# Create your views here.
def index(request):
    # Define the number of items per page
    items_per_page = 3

    # Create a Paginator object
    paginator = Paginator(questions, items_per_page)

    # Get the page number from the request
    page_number = request.GET.get('page')

    # Get the desired page
    page_obj = paginator.get_page(page_number)

    # Render the page, passing the page object
    return render(request, 'index.html', {'page_obj': page_obj})

def question(request, question_id):
    item = questions[question_id]
    return render(request, template_name='question.html', context={'question': item})

