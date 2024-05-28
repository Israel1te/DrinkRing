from django import forms
from .models import Session
from django.forms import modelformset_factory
from .models import Player

class SessionForm(forms.ModelForm):
    num_players = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Enter number of players'}),
        label='Number of Players',
        min_value=2,
        max_value=15  # Maximum 15 players
    ) 

    class Meta:
        model = Session
        fields = ['num_players']
        labels = {
            'num_players': "How many players?",
        }

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name']

PlayerFormSet = modelformset_factory(Player, form=PlayerForm, extra=0)