from django.shortcuts import render
from django.http import HttpResponse
import flights
from flights.models import Flight

# Create your views here.

origem=Flight.origin="BH"
destino=Flight.destination="SP"
duracao=Flight.duration=120

table = [
    origem,
    destino,
    duracao
]

def index(request):
    return render(request, "flights/index.html", {
        "origem":origem,
        "destino":destino,
        "duracao":duracao,
        "tabela":table

    })
