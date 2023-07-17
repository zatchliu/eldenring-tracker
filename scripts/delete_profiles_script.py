from characters.models import Character

def run():
    Character.objects.all().delete()