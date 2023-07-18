import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Character, Boss
from .forms import CharacterName, CharacterProfileForm, CharacterForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def home(request):
  return redirect(login_user)

def logout_user(request):
    logout(request)
    return redirect(login_user)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login_user)
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(character_list) 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def delete_character(request, character_id):
    character = get_object_or_404(Character, id=character_id)

    # Ensure the user owns the character before allowing deletion
    if character.user != request.user:
        return JsonResponse({'status': 'error', 'message': 'You are not authorized to delete this character.'}, status=403)

    if request.method == 'DELETE':
        character.delete()
        return JsonResponse({'status': 'success', 'message': 'Character deleted successfully.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid method.'}, status=400)

@login_required
def character_list(request):
  character_name=None
  user= request.user
  characters = Character.objects.filter(user=request.user)
  form = CharacterName(request.POST or None)

  if request.method == 'POST':
    if form.is_valid():
      character_name = form.cleaned_data['character_name']
      character_class = form.cleaned_data['character_class']

      #Getting stats from Elden Ring API
      url = 'https://eldenring.fanapis.com/api/classes'
      response = requests.get(url)

      if response.status_code == 200:
        characters_data = response.json()['data']
        for character_data in characters_data:
          if character_data['name'] == character_class:
            character_level=character_data['stats']['level']
            new_character=Character.objects.get_or_create(user=user,
                                                          name=character_name,
                                                          level=character_level,
                                                          class_name=character_class,
                                                          vigor=character_data['stats']['vigor'],
                                                          mind=character_data['stats']['mind'],
                                                          endurance=character_data['stats']['endurance'],
                                                          strength=character_data['stats']['strength'],
                                                          dexterity=character_data['stats']['dexterity'],
                                                          intelligence=character_data['stats']['intelligence'],
                                                          faith=character_data['stats']['faith'],
                                                          arcane=character_data['stats']['arcane'],
                                                          )
            character_id=new_character[0].id
            return redirect('characterprofile', character_id=character_id)
          
  return render(request, 'characters.html', {'characters': characters, 'form': form})

@login_required
def characterprofile(request, character_id):
  all_bosses=Boss.objects.all()
  boss_by_region={}

  #Mapping bosses by region
  for boss in all_bosses:
    if boss.region not in boss_by_region:
      boss_by_region[boss.region]=[]
    boss_by_region[boss.region].append(boss)

  character = get_object_or_404(Character, id=character_id)
  if character.user != request.user:
        return redirect('character_list')
  name = character.name
  level=character.level
  class_name = character.class_name
  form = CharacterProfileForm(request.POST or None, instance=character)

  if request.method == 'POST':
    if form.is_valid():
      character=form.save()
      completed_bosses_ids = request.POST.getlist('completed_bosses')
      character.completed_bosses.set(completed_bosses_ids)
      return redirect('characterprofile', character_id=character_id)

  return render(request, 'profile.html', {'form': form, 
                                          'level':level,
                                          'class_name':class_name,
                                          'character': character, 
                                          'name':name, 
                                          'all_bosses':all_bosses,
                                          'boss_by_region':boss_by_region,
                                          })

