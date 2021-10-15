from django.shortcuts import render
from flights.models import Flight

# Create your views here.

f= Flight(origin="BH", destination="SP", duration=120) 
f.save()

flight0=Flight.objects.all()

def index(request):
    return render(request, 'flights/index.html', {
        "flight0":flight0
    })