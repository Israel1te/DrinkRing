from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing_page.html')

def settings(request):
    return render(request, 'settings.html')

def cards(request):
    return render(request, 'cards.html')