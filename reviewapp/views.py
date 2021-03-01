from django.shortcuts import render

# Create your views here.

def listfunc(request):
    return render(request, 'reviewapp/list.html', {})