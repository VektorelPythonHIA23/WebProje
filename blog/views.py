from django.shortcuts import render



def gonderListe(request):
    return render(request,"blog/gonderilist.html",{})