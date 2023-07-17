from characters.models import Boss

def run():
    Boss.objects.all().delete()