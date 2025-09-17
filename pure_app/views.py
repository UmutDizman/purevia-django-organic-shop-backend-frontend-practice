from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pure_app/index.html')