from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing.html')

def timeline(request):
    return render(request, 'timeline.html')

