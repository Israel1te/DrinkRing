from django.contrib import admin
from django.urls import path, include
from DrinkGame import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),
    path('settings', views.settings, name='settings'),
    path('cards', views.cards, name='cards'),
    path('phase-one/', views.phase_one, name='phase_one'),
    path('phase-two/', views.phase_two, name='phase_two'),
    path('phase-three/', views.phase_three, name='phase_three'),
    path('', include('django.contrib.auth.urls')),
    path('sign-up/', views.sign_up, name='sign_up')
]