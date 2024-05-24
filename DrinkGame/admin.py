from django.contrib import admin
from .models import Card
from .models import Session, Player

admin.site.register(Card)

class PlayerInline(admin.TabularInline):
    model = Player
    extra = 1

class SessionAdmin(admin.ModelAdmin):
    inlines = [PlayerInline]

admin.site.register(Session, SessionAdmin)