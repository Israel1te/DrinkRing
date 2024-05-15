from django.contrib import admin
from django.urls import path
from DrinkGame import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),
    path('', views.settings, name='settings'),
    path('', views.cards, name='cards'),
]