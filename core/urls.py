from django.urls import path
from .views import index, contato, produto

urlpatterns = [
    #se for para raiz manda pra views index
    path('', index, name= 'index'),
    #se for pra contato manda pra views contato
    path('contato', contato, name= 'contato'),
    path('produto/<int:pk>', produto, name= 'produto'),
]
