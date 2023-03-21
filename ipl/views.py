from django.shortcuts import render

# Create your views here.
def ipl(request):
    return render(request,'ipl.html')