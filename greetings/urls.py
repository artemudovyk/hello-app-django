from django.urls import path
from . import views

app_name = 'greetings'

urlpatterns = [
    path('', views.home, name='home'),
    path('who-came-before-you/', views.greetings_history, name='history')
]