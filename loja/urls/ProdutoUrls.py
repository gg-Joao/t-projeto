from django.urls import path
from ..views import produto_view

urlpatterns = [
    path('', produto_view, name='produto_sem_id'),
    path('<int:id>/', produto_view, name='produto_com_id'),
]