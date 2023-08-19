from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    # checar autenticação
    if request.method == 'POST':
        Usuario = request.POST['username']
        Senha = request.POST['password']
        user = authenticate(request, username=Usuario, password=Senha)
        if user is not None:
            login(request, user)
            messages.success(request, 'Você logou no site!')
            return redirect('home')
        else:
            messages.success(request, 'Alguma coisa deu errado, tente novamente!')
            return redirect('home')

    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'Você saiu da plataforma...')
    return redirect('home')

 