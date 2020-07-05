from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from Control.static.credential import spreads
from google.oauth2 import id_token
from google.auth.transport import requests
import urllib, json
from django.conf import settings

def logar(request):
    return render(request, 'login.html', {'site_key': settings.RECAPTCHA_SITE_KEY})

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
        # Init reCAPTCHA:
        dados = {
        'response': request.POST.get('g-recaptcha-response'),
        'secret': settings.RECAPTCHA_SECRET_KEY
        }
        url = 'https://www.google.com/recaptcha/api/siteverify'
        data = urllib.parse.urlencode(dados).encode() # Codifica os dados
        requisicao = urllib.request.Request(url, data=data) # Realiza a requisição com os dados codificados
        response = urllib.request.urlopen(requisicao) # Obtém a resposta
        result = json.loads(response.read().decode()) # Decodifica a resposta
        if result['score'] == 0.0:
            error = 'reCAPTCHA inválido'
            context = {"error": error}
            return render(request, 'login.html', context)
        # End reCAPTCHA:
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