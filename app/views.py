from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'suneel','age': 24}
    return render(request,'wish.html',context=d)

    
def conditions(request):
    d={'a':100,'b':50}
    return render(request,'conditions.html',context=d)
