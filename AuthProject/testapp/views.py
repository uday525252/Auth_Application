from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home_view(request):
    return render(request,"home.html")



def java_view(request):
    return render(request,"java.html")

@login_required
def python_view(request):
    return render(request,"python.html")

@login_required
def aptitude_view(request):
    return render(request,"aptitude.html")
