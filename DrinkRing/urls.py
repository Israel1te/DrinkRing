from django.contrib import admin
from django.urls import path, include
from DrinkGame import views
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.register, name='register'),
    path('', include("django.contrib.auth.urls")),
    path('', views.landing_page, name='landing_page'),
    path('settings/', views.settings, name='settings'),
    path('cards/', views.cards, name='cards'),
    path('phase-one/', views.phase_one, name='phase_one'),
    path('phase-two/', views.phase_two, name='phase_two'),
    path('phase-three-quick/', views.phase_three_quick, name='phase_three_quick'),
    #path('create_session/', views.create_session, name='create_session'),
    path('add_players', views.add_players, name='add_players'),
    #path('session_detail/<int:session_id>/', views.session_detail, name='session_detail'),
]