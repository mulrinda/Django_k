from django.shortcuts import render,redirect

# Create your views here.

def test(request):
    return render(request, 'tothers/theme1.html')
