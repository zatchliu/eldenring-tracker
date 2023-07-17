import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Character, Boss
from .forms import CharacterName, CharacterProfileForm

def home(request):
  return redirect(character_list)

def character_list(request):
  character_name=None
  characters = Character.objects.all()
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
            new_character=Character.objects.get_or_create(name=character_name,
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

def characterprofile(request, character_id):
  all_bosses=Boss.objects.all()
  boss_by_region={}

  #Mapping bosses by region
  for boss in all_bosses:
    if boss.region not in boss_by_region:
      boss_by_region[boss.region]=[]
    boss_by_region[boss.region].append(boss)

  character = get_object_or_404(Character, id=character_id)
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

