from django.shortcuts import render

def index(request):
    return render(request, 'user_app/index.html')

# Create your views here.
