from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'airbnb'
urlpatterns = [
    #com o auth_views consigo de forma fácil fazer login e logout usando já a ferramenta do django pronta pra isso
    #como parâmetro é passado o template dessa página
    path('', auth_views.LoginView.as_view(template_name='airbnb/index.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='airbnb/logout.html'), name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
]
