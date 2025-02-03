from django.urls import path
#from generales import views #importamo views porque es a la que le vamos a asociar una url 
from .views import productos
#import usuarios.views
urlpatterns = [
    path('', productos,name="productos"),#Le asociamos a la funcion index la url ''
#    path('users/', usuarios.views.usuarios,name="usuarios")
]