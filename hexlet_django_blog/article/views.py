from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    tags = 'mikl'
    return render(
        request,
        'index.html',
        context={'who': tags},
    )
# Create your views here.
