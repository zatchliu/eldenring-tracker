from django.urls import path
from . import views

urlpatterns = [
    path('characters/', views.character_list, name='character_list'),
    path('', views.home, name='home'),
    #path('characters/profile/<int:character_id>/', views.characterprofile, name='characterprofile'),
]
