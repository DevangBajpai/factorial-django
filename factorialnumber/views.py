from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello, Please add a number in URL parameter. Example: /5/ or /factorial?number=5/")

# Calculate factorial using /<int:number>/
def calculateFactorial(request,number):
    factorial = 1
    for i in range(1,number+1):
        factorial = factorial * i
    return HttpResponse("Factorial of " + str(number) + " is " + str(factorial))

# Calcualte factorial using /factorial?number=<int:number>/
def paramFactorial(request):
    number = int(request.GET.get('number'))
    factorial = 1
    for i in range(1,number+1):
        factorial = factorial * i
    return HttpResponse("Factorial of " + str(number) + " is " + str(factorial))
    