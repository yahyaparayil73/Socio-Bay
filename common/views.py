from django.shortcuts import render

# Create your views here.

def common_home(request):
    return render(request,'common_home.html')
