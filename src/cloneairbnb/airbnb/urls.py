from django.urls import path
from . import views

app_name = 'airbnb'
urlpatterns = [
    path('', views.login, name='login'),
]
