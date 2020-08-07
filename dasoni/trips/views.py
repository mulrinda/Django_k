from django.shortcuts import render

# Create your views here.
def spotchart(request):
    return render(request, 'trips/spotchart.html')