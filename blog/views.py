from django.shortcuts import render
from blog.models import Vprasanje

# Create your views here.
def prva_stran(request):
    return render(request, 'prva.html', {})

def lepsa_stran(request):
    return render(request, 'index.html', {})

def domaca_stran(request):
    return render(request, 'homepage.html', {})

def blog_stran(request):
    return render(request, 'blog.html', {})

def galerija_stran(request):
    return render(request, 'galerija.html', {})

def onas_stran(request):
    return render(request, 'onas.html', {})

def kontakti_stran(request):
    return render(request, 'kontankti.html', {})

def vprasanje(request, id=1):
    vprasanje = Vprasanje.objects.get(pk=id)
    print(vprasanje)
    return render(request, 'vprasanje.html', {"vprasanje": vprasanje})
