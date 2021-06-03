from django.contrib import admin
from django.urls import path
from .views import index, perros, gatos, scooby, patan, coraje, doraemon, tom, garfield ##IMPORTANTE ESCRIBIR DIRECCION.VIEWS IMPORT INDEX

##from webAyudaPeludo import views ##index, perros, gatos, scooby, patan, coraje, doraemon, tom, garfield ##IMPORTANTE ESCRIBIR DIRECCION.VIEWS IMPORT INDEX

urlpatterns = [
    path('',index,name="INDEX"),
    ##seccion perros
    path('perros/',perros,name="PERROS"),
    path('scooby/',scooby,name="SCOOBY"),
    path('patan/',patan,name="PATAN"),
    path('coraje/',coraje,name="CORAJE"),
    ##seccion gatos
    path('gatos/',gatos,name="GATOS"),
    path('doraemon/',doraemon,name="DORAEMON"),
    path('tom/',tom,name="TOM"),
    path('garfield/',garfield,name="GARFIELD"),
]

# {% url '<nombre>' %} --> LENGUAJE DJANGO TEMPLATE