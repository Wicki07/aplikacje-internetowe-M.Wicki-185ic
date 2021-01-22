from django.shortcuts import render

def index(request):
    return render(request, 'worker1/index.html')

def index2(request):
    return render(request, 'worker2/index.html')
