from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def trans(request):
    return render(request,'trans.html')