from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.


def signupfunc(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(username, '', password)
            return redirect('../../reviewapp/list')
        except IntegrityError:
            return render(request, 'usermanage/signup.html', {'error':'このユーザーは登録されています。'})
    return render(request, 'usermanage/signup.html', {})

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../../reviewapp/list')
        else:
            return render(request, 'usermanage/login.html', {})
    return render(request, 'usermanage/login.html')

def logoutfunc(request):
    logout(request)
    return redirect('../../usermanage/login')