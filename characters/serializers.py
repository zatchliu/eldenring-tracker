from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Character
        fields = ['id', 'name', 
                  'level','class_name',
                  'vigor', 'mind', 
                  'endurance', 'strength', 
                  'dexterity', 'intelligence', 
                  'faith', 'arcane', 
                  'completed_bosses', 'user',
                  ]