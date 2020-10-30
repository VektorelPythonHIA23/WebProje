from django.shortcuts import render,get_object_or_404
from .models import GonderiModel
from .forms import GonderiForm

def gonderListe(request):
    gonderiler = GonderiModel.objects.all()
    return render(request,"blog/gonderilist.html",{"gonderis":gonderiler})

def gonderiDetay(request,pk):
    # gonderi = GonderiModel.objects.get(pk=pk)
    gonderi = get_object_or_404(GonderiModel,pk=pk)
    return render(request,"blog/gonderidetay.html",{"gonderi":gonderi})


def yeniGonderi(request):
    form = GonderiForm()
    return render(request,"blog/yenigonderi.html",{"form":form})