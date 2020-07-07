from django.shortcuts import render
from django.core import serializers
from .models import Silaba, Metrica, Comentario
from .forms import ComentarioForm
from datetime import datetime
import random

list_silabas = []
list_sorteadas = []

def serialize_object(obj):
    return serializers.serialize('xml', obj)
    
def deserialize_object(obj):
    silaba_obj = []
    for d_obj in serializers.deserialize('xml', obj):
        silaba_obj.append(d_obj.object)
    return silaba_obj

def home(request):
    global list_silabas
    global list_sorteadas
    list_sorteadas = []
    list_silabas = []
    list_silabas = list(Silaba.objects.all())
    request.session['sorteadas'] = serialize_object(list_sorteadas)
    request.session['silabas'] = serialize_object(list_silabas)
    return render(request, 'home.html')

def publicar_metrica():
    mes_hoje = datetime.today().month
    ano_hoje = datetime.today().year
    return Metrica.objects.filter(mes=mes_hoje,ano=ano_hoje)

def silaba_escolhida(lista):
    silaba = random.choice(lista)
    lista.remove(silaba)
    return silaba

def sortear(request):
    session_escolhida = None
    session_sorteadas = None
    metrica = publicar_metrica()
    n_sorteio = metrica[0].sorteios + 1
    metrica.update(sorteios=n_sorteio)
    global list_silabas
    global list_sorteadas
    if len(list_silabas) == 0:
        silaba_escolhida = None
    else:
        silaba_escolhida = random.choice(list_silabas)
        list_silabas.remove(silaba_escolhida)
        list_sorteadas.append(silaba_escolhida)
        if silaba_escolhida != None:
            request.session['escolhida'] = serialize_object([silaba_escolhida])
        request.session['sorteadas'] = serialize_object(list_sorteadas)
        request.session['silabas'] = serialize_object(list_silabas)
        session_escolhida = deserialize_object(request.session.get('escolhida'))
        session_sorteadas = deserialize_object(request.session.get('sorteadas'))
    return render(request, 'sorteio.html', {
        'silaba_escolhida': session_escolhida,
        'sorteadas': session_sorteadas,
    })

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
    metrica = publicar_metrica()
    if rede == 'facebook':
        n_facebook = metrica[0].facebook + 1
        metrica.update(facebook=n_facebook)
    elif rede == 'twitter':
        n_twitter = metrica[0].twitter + 1
        metrica.update(twitter=n_twitter)
    elif rede == 'whatsapp':
        n_whatsapp = metrica[0].whatsapp + 1
        metrica.update(whatsapp=n_whatsapp)
    elif rede == 'telegram':
        n_telegram = metrica[0].telegram + 1
        metrica.update(telegram=n_telegram)
    elif rede == 'email':
        n_email = metrica[0].email + 1
        metrica.update(email=n_email)
    return render(request, 'compartilhamento.html', {
        'rede': rede,
    })

def comentario(request):
    novo_comentario = None
    if request.method == 'POST':
        comentario_form = ComentarioForm(data=request.POST)
        if comentario_form.is_valid():
            novo_comentario = comentario_form.save(commit=False)
            novo_comentario.save()
    else:
        comentario_form = ComentarioForm()
    return render(request, 'comentario.html', {
        'novo_comentario': novo_comentario,
        'comentario_form': comentario_form
    })