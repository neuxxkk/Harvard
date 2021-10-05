from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    return render(request, "whattime/index.html", {
        "minute":now.minute,
        "hour":now.hour,
        "day":now.day,
        "month":now.month,
        "year":now.year
    })