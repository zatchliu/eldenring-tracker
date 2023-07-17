import requests
from characters.models import Boss

def fetch_boss_data():
    url = 'https://eldenring.fanapis.com/api/bosses?limit=106'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        return None

def run():
    boss_data = fetch_boss_data()
    if boss_data:
        for boss in boss_data:
            name=boss['name']
            region=boss['region']
            location=boss['location']
            if not Boss.objects.filter(name=name).exists():
                if name=='Erdtree Avatar' or name=='Bell Bearing Hunter':
                    region='Reoccuring Bosses'
                if name=='Commander Niall':
                    region='Mountaintops of the Giants'
                Boss.objects.create(name=name, region=region, location=location)