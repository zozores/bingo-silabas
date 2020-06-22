from django.shortcuts import render
from .models import Silaba, Compartilhamento
from datetime import datetime
import random

list_silabas = []
list_sorteadas = []

def home(request):
    global list_silabas
    global list_sorteadas
    list_sorteadas = []
    list_silabas = []
    list_silabas = list(Silaba.objects.all())
    return render(request, 'home.html')

def sortear(request):
    global list_silabas
    global list_sorteadas
    if len(list_silabas) == 0:
        silaba_escolhida = None
    else:
        silaba_escolhida = random.choice(list_silabas)
        list_silabas.remove(silaba_escolhida)
        list_sorteadas.append(silaba_escolhida)
    return render(request, 'sorteio.html', {
        'silaba_escolhida': silaba_escolhida,
        'sorteadas': list_sorteadas,
    })

def silaba_escolhida(lista):
    silaba = random.choice(lista)
    lista.remove(silaba)
    return silaba

def cartelas(request):
    dic = {}
    for i in range(6):
        lista = list(Silaba.objects.all())
        arr = [[ silaba_escolhida(lista).silaba for n in range(4) ] for n in range(3)]
        dic[i] = arr
    return render(request, 'cartelas.html',{
        'dic': dic,
    })

def compartilhar(request, rede):
    mes_hoje = datetime.today().month
    ano_hoje = datetime.today().year
    cid = Compartilhamento.objects.filter(mes=mes_hoje,ano=ano_hoje)
    if rede == 'facebook':
        n_facebook = cid[0].facebook + 1
        cid.update(facebook=n_facebook)
    elif rede == 'twitter':
        n_twitter = cid[0].twitter + 1
        cid.update(twitter=n_twitter)
    elif rede == 'whatsapp':
        n_whatsapp = cid[0].whatsapp + 1
        cid.update(whatsapp=n_whatsapp)
    elif rede == 'telegram':
        n_telegram = cid[0].telegram + 1
        cid.update(telegram=n_telegram)
    elif rede == 'email':
        n_email = cid[0].email + 1
        cid[0].update(email=n_email)
    return render(request, 'compartilhamento.html', {
        'rede': rede,
    })