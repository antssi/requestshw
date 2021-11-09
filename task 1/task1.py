import requests
from pprint import pprint

super_heroes = ['Hulk', 'Thanos', 'Captain America']
API_KEY = '2619421814940190'

def most_intelligent(heroes):
    url_pack = []
    intelligence_dict = {}
    uri = 'https://superheroapi.com/api/'
    acces_token = API_KEY
    max = 0

    for hero in heroes:
        uri2 = '/search/' + hero
        full_url = uri + acces_token + uri2
        url_pack.append(full_url)

    for url in url_pack:
        timeout = 5
        res = requests.get(url=url, timeout=timeout)
        name = res.json()["results-for"]
        intelligence = int(res.json()["results"][0]['powerstats']['intelligence'])
        intelligence_dict[name] = intelligence

    for max_int in intelligence_dict.items():
        if max_int[1] > max:
            max = max_int[1]
            smartest_hero = max_int [0]
    print(f'Наибольший показатель интеллекта у {smartest_hero} - {max}')

most_intelligent(super_heroes)