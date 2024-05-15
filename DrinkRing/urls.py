from django.contrib import admin
from django.urls import path
from DrinkGame import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),
    path('', views.settings, name='settings'),
    path('', views.cards, name='cards'),
    path('phase-one/', views.phase_one, name='phase_one'),
    path('phase-two/', views.phase_two, name='phase_two'),
    path('phase-three/', views.phase_three, name='phase_three'),
]