from django.shortcuts import render, redirect
from .models import Session, Player
from .forms import SessionForm, PlayerFormSet
from django.contrib.auth.decorators import login_required
from .models import Card

def landing_page(request):
    if request.method == 'POST':
        existing_session = Session.objects.filter(user=request.user).first()
        if existing_session:
            return redirect('phase_one')
        else:
            session = Session.objects.create(user=request.user, num_players=0)
            return redirect('phase_one')
    return render(request, 'landing_page.html')

def update_players(request):
    session = Session.objects.filter(user=request.user).first()
    if request.method == 'POST':
        new_num_players = int(request.POST.get('num_players'))
        session.num_players = new_num_players
        session.save()
        return redirect('phase_2')
    return render(request, 'phase_one_players.html')

def settings(request):
    return render(request, 'settings.html')

def cards(request):
    return render(request, 'cards.html')

def phase_one(request):
    template_name = 'phase_one_players.html'
    session = Session.objects.filter(user=request.user).first()
    if request.method == 'POST':
        new_num_players = int(request.POST.get('num_players'))
        session.num_players = new_num_players
        session.save()
        return redirect('phase_two')
    return render(request, template_name)

def phase_two(request):
    template_name = 'phase_two_mode.html'
    return render(request, template_name)

def phase_three(request):
    cards = Card.objects.all()
    template_name = 'phase_3_game.html'
    return render(request, template_name, {'cards':cards})

