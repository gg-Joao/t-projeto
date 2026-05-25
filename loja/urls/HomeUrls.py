from django.urls import path
from django.http import HttpResponse


def home(request):
    return HttpResponse('Loja Home')


urlpatterns = [
    path('', home, name='home'),
]
from django.urls import path
from ..views import home_view

urlpatterns = [
    path('', home_view, name='home'),
]