from django.shortcuts import render

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