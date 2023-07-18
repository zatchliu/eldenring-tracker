from django.urls import path
from . import views
from .api_views import CharacterListCreateAPIView, CharacterRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('characters/', views.character_list, name='character_list'),
    path('', views.home, name='home'),
    path('characters/profile/<int:character_id>/', views.characterprofile, name='characterprofile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('delete/<int:character_id>/', views.delete_character, name='delete_character'),
    path('api/charactersapi/', CharacterListCreateAPIView.as_view(), name='character-list-create'),
    path('api/charactersapi/<int:pk>/', CharacterRetrieveUpdateDestroyAPIView.as_view(), name='character-retrieve-update-destroy'),
]
