import requests

def get_heroes_info():
    url = f'https://superheroapi.com/api/2619421814940190/search/{name}'
    response = requests.get(url)
    dict = response.json()['results']
    return dict

def get_heroes_intelligence():
    dict_hero = get_heroes_info()
    for character in dict_hero:
        if character['name'] == name:
            if 'powerstats' in character:
                intelligence_hero[name] = character['powerstats']['intelligence']
            else:
                continue
        else:
            continue

if __name__ == '__main__':
    list_hero = ['Hulk', 'Captain America', 'Thanos']
    intelligence_hero = {}
    for name in list_hero:
        get_heroes_intelligence()
    most_intelligence = sorted(intelligence_hero.items(), key=lambda x: x[1])
    print(f'Самый умный супергерой:{most_intelligence[0]}')




