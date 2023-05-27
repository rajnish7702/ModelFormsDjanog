from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    form = forms.GeeksForms
    if(request.method=="POST"):
        form = forms.GeeksForms(request.POST)
        if(form.is_valid()):
            form.save()
    return render(request,'index.html',{'form':form})