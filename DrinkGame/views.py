from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate

def landing_page(request):
    return render(request, 'landing_page.html')

def settings(request):
    return render(request, 'settings.html')

def cards(request):
    return render(request, 'cards.html')


def phase_one(request):
    template_name = 'phase_one_players.html'
    return render(request, template_name)

def phase_two(request):
    template_name = 'phase_two_mode.html'
    return render(request, template_name)

def phase_three(request):
    template_name = 'phase_3_game.html'
    return render(request, template_name)

def sign_up(request):
    if request.method== 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return (redirect('/'))
    else: 
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {"form": form})