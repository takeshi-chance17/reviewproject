from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import ReviewModel

# Create your views here.

def listfunc(request):
    object_list = ReviewModel.objects.all()
    return render(request, 'reviewapp/list.html', {'object_list': object_list})

def detailview(request, pk):
    object = ReviewModel.objects.get(pk=pk)
    return render(request, 'reviewapp/detail.html', {'object': object})

class Create(CreateView):
    template_name = 'reviewapp/create.html'
    model = ReviewModel
    fields = ('title', 'content', 'author', 'image', 'evaluation')
    success_url = reverse_lazy('list')

def goodfunc(request, pk):
    object = ReviewModel.objects.get(pk=pk)
    username = request.user.get_username()
    print('#######################################')
    print(username)
    print(object.useful_review_record)
    if username in object.useful_review_record:
        return redirect('list')
    else:
        object.useful_review += 1
        object.useful_review_record += " " + username
        object.save()
        return redirect('list')