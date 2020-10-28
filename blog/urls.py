from django.urls import path
from . import views

urlpatterns = [
    path('',views.gonderListe,name="gonderListe"),
    path('detay/<int:pk>',views.gonderiDetay,name="gonderiDetay"),
    
]