from django.urls import path
from .views import *
urlpatterns={
    path('', index, name="blog"),
    path('entrada/crear', crea_entrada, name="crea_entrada"),
    
}
