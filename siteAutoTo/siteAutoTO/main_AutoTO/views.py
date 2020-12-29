from django.shortcuts import render
from django import forms

# Create your views here.
def index(request):
    return render(request, 'main_AutoTO/homePage.html')
    f = forms.Select(choices=(xc40, xc60, xc90))
