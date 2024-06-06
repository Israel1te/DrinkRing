from django.shortcuts import render, redirect
from .models import Session, Player
from .forms import SessionForm, PlayerFormSet
from django.contrib.auth.decorators import login_required
from .models import Card
from django.http import JsonResponse
import random

def add_players(request):
    session = Session.objects.filter(user=request.user).first()
    #deleting all existing players
    session.players.all().delete()
    player_range = range(1, session.num_players + 1)
    players = session.players.all()
    if request.method == 'POST':
        for i in player_range:
            name = request.POST.get(f'player_{i}')
            Player.objects.create(session=session, name=name, points=0)
        players = session.players.all()
        return redirect('phase_two')
    return render(request, 'add_players.html', {'session': session, 'players': players, 'player_range': player_range})

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
        return redirect('add_players')
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
        return redirect('add_players')
    return render(request, template_name)

def phase_two(request):
    template_name = 'phase_two_mode.html'
    return render(request, template_name)

def phase_three_quick(request):
    cards = Card.objects.all()
    session = Session.objects.filter(user=request.user).first()
    players = session.players.all()
    template_name = 'phase_3_quick.html'
    return render(request, template_name, {'cards':cards, 'session': session, 'players': players})

def card_view(request):
    card_bodies = list(Card.objects.values_list('body', flat=True))
    random.shuffle(card_bodies)
    request.session['cards'] = card_bodies
    request.session['index'] = 0
    return render(request, 'game/card.html')

def get_card(request):
    if 'cards' not in request.session or 'index' not in request.session:
        card_bodies = list(Card.objects.values_list('body', flat=True))
        random.shuffle(card_bodies)
        request.session['cards'] = card_bodies
        index = 0
    else:
        card_bodies = request.session['cards']
        index = request.session['index']
        
        if index >= len(card_bodies):
            random.shuffle(card_bodies)
            request.session['cards'] = card_bodies
            index = 0

    card_body = card_bodies[index]
    request.session['index'] = index + 1
    return JsonResponse({'body': card_body, 'index': request.session['index']})

