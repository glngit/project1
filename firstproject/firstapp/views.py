from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    s='<h1>Hello students welcome to Durgasoft Django classes!!!</h1>'
    return HttpResponse(s)
