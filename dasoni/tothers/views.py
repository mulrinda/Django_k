from django.shortcuts import render,redirect

def goods(request):
    return render(request,'tothers/goods.html')

def tourtip(request):
    return render(request,'tothers/tourtip.html')
