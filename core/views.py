from django.shortcuts import render
from .models import Silaba
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
