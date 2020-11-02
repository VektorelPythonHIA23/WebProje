from django.shortcuts import render,get_object_or_404,redirect
from .models import GonderiModel
from .forms import GonderiForm
from django.contrib.auth.models import User
from django.utils import timezone

def gonderListe(request):
    gonderiler = GonderiModel.objects.all()
    return render(request,"blog/gonderilist.html",{"gonderis":gonderiler})

def gonderiDetay(request,pk):
    # gonderi = GonderiModel.objects.get(pk=pk)
    gonderi = get_object_or_404(GonderiModel,pk=pk)
    return render(request,"blog/gonderidetay.html",{"gonderi":gonderi})


def yeniGonderi(request):
    if request.method == "POST":
        form = GonderiForm(request.POST)
        if form.is_valid():
            gonderi = form.save(commit=False)
            gonderi.yazar = request.user
            gonderi.yayim_zaman = timezone.now()
            gonderi.save()
            return redirect('gonderListe')
    else:
        form = GonderiForm()
    return render(request,"blog/yenigonderi.html",{"form":form})


def gonderiDuzenle(request,pk):
    gonderi = get_object_or_404(GonderiModel,pk=pk)
    if request.method == "POST":
        form = GonderiForm(request.POST,instance=gonderi)
        if form.is_valid():
            gonderi = form.save(commit=False)
            ben = User.objects.get(username="admin")
            gonderi.yazar = ben
            gonderi.yayim_zaman = timezone.now()
            gonderi.save()
            return redirect('gonderListe')
    else:
        form = GonderiForm(instance=gonderi)
    return render(request,"blog/yenigonderi.html",{"form":form})