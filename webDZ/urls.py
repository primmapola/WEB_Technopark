from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='mainView'),
    path('question/<int:question_id>', views.question, name='questionView'),
    path('ask', views.ask, name='askView'),
    path('tagged/<str:tag_name>/', views.tagged_questions, name='tagged_questions'),
    path('settings', views.settings, name='settingsView'),
    path('login', views.login, name='loginView'),
    path('signup', views.signup, name='signupView'),
    path('admin/', admin.site.urls),
]
