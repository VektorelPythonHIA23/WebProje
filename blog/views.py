from django.shortcuts import render,get_object_or_404
from .models import GonderiModel


def gonderListe(request):
    gonderiler = GonderiModel.objects.all()
    return render(request,"blog/gonderilist.html",{"gonderis":gonderiler})

def gonderiDetay(request,pk):
    gonderi = get_object_or_404(GonderiModel,pk=pk)
    return render(request,"blog/gonderidetay.html",{"gonderi":gonderi})
