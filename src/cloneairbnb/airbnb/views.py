from django.shortcuts import render, redirect
from .models import Cliente
from .forms import UserRegisterForm
from django.contrib import messages

def cadastro(req):
    if req.method == 'POST':
        form = UserRegisterForm(req.POST) #se tenho uma requisição POST crie o formulário com os dados dessa requisição
        if form.is_valid():
            form.save() #salve de fato os dados no backend automaticamente e cria o usuário
            #username = form.cleaned_data.get('username') era usado para a mensagem abaixo
            messages.success(req, f'Conta criada com sucesso! Você está apto a logar')
            return redirect('airbnb:login')
    else:
        form = UserRegisterForm() #se não, crie um formulário novo
    return render(req, 'airbnb/cadastre.html', {'form': form})

def homepage(req):
    return render(req, 'airbnb/homePage.html')