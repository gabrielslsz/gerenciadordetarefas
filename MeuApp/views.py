from django.shortcuts import render, HttpResponse

# Create your views here.

def soma(request, numer_a, numer_b):
    total = numer_a + numer_b 
    return HttpResponse('<h1>Hello {}</h1>'. format(total)) 