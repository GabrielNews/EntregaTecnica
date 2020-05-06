from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from Control.static.credential import spreads

def logar(request):
    return render(request, 'login.html')

def deslogar(request):
    logout(request)
    return redirect('/logar/')

def direcionar(request):
    return redirect('/logar/')

def autenticar(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        acesso = authenticate(username=usuario, password=senha)
        if acesso is not None:
            login(request, acesso)
            return redirect('consultar/')
        else:
            error = "Usuário e/ou Senha inválidos. Por favor, tente novamente!"
            context = {"error": error}
    return render(request, 'login.html', context)

@login_required(login_url='/logar/')
def consultar(request):
    consulta = spreads.Todos()
    context = { 'consulta': consulta }
    return render(request, 'consulta.html', context)

def jsonResponse(request):
    consulta = spreads.Status(status)
    context = { 'consulta': consulta }
    return render(request, 'consulta.html', context)