from django import forms
from .models import Character
import requests

class CharacterName(forms.Form):
    character_name = forms.CharField(label='Enter Your Character Name', max_length=100)
    character_class = forms.ChoiceField(label='Select Character Class', choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['character_class'].choices = self.get_character_classes()

    def get_character_classes(self):
        url = 'https://eldenring.fanapis.com/api/classes'
        response = requests.get(url)
        if response.status_code == 200:
            choices=[]
            classes_data = response.json()['data']
            for class_data in classes_data:
                c=class_data['name']
                choices.append((c,c))
            return choices
        return []

class CharacterProfileForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['vigor', 
                  'mind', 
                  'endurance', 
                  'strength', 
                  'dexterity', 
                  'intelligence', 
                  'faith', 
                  'arcane',
                  ]