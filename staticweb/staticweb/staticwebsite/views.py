from django.shortcuts import render
from .models import Place, Teams


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj2 = Teams.objects.all()
    return render(request, 'index.html', {'result': obj, 'result2': obj2})
