from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('', views.index, name = 'mainView'),
    path('question/<int:question_id>', views.question, name = 'questionView'),
    path('admin/', admin.site.urls),
]
