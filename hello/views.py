from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'template1.html')

def run(request):
    num = int(request.GET['num'])
    #Odd-Even
    if num%2 == 0:
        oeans = 'Even'
    else: oeans = 'Odd'

    #Prime-Composite
    if num == 1 or num == 0:
        pcans = 'Neither Prime nor Composite'
    elif num == 2:
        pcans = 'Prime'
    else:
        for i in range(2,num):
            if num%i == 0:
                pcans = 'Composite'
                break
            else: pcans = 'Prime'

    #Digits
    for i in range(100):
        if num == 1:
            i  = 1
        elif num <= 10**i:
            break
    return render(request, 'oeans.html', {'oeans':oeans, 'pcans':pcans, 'digit': i})