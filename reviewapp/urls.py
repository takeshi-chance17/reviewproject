from django.urls import path
from .views import listfunc, detailview, Create, goodfunc

urlpatterns = [
    path('list/', listfunc, name='list'),
    path('detail/<int:pk>/', detailview, name='detail'),
    path('create/', Create.as_view(), name='create'),
    path('good/<int:pk>/', goodfunc, name='good'),
]
