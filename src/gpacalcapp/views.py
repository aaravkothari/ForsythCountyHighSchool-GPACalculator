from django.shortcuts import render
from django.http import HttpResponse
from .models import CurrentGPA
from .models import Course


# Create your views here.
def index(request):
    return render(request, 'interface.html', {})

"""def submitquery(request):
    q = request.GET['query']
    return HttpResponse(q)"""