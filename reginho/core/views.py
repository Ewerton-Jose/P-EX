from django.shortcuts import render, get_object_or_404
from .models import Regi

# Create your views here.
def principal(request):
    regis = Regi.objects.all()
    return render(request, 'reginho/index.html', {'regis': regis})

def regiview(request, id):
    regi = get_object_or_404(Regi, pk=id)
    return render(request, 'reginho/regi.html', {'regi':regi})
