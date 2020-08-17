from django.shortcuts import render
from googletrans import Translator
from groups.models import Star

# Create your views here.
def translate(request):
    # translator = Translator()
    # result = translator.translate('안녕하세요')
    context = {
        "text" : '안녕하세요'
    }
    return render(request, 'maps/translate.html', context=context)

def index(request):
  return render(request,'maps/index.html')


def rankingtest(request):
    return render(request, 'maps/rankingtest.html')


def weather(request):
    return render(request,'maps/weather.html')


def categorysing(request):
    return render(request, 'maps/categorysing.html')


def categorydrama(request):
    return render(request, 'maps/categorydrama.html')


def categoryenter(request):
    return render(request, 'maps/categoryenter.html')

def stars(request):
    stars = Star.objects.all()
    context = {
        'stars' : stars
    }
    return render(request, 'maps/stars.html')