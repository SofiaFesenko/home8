import requests
import csv

base_url = 'https://anekdot-ua.net/'


def get_html_from_url(url):
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(url=url, headers=headers)
    return response.text


with open('source.html', mode='a') as file:
    file.write(get_html_from_url(base_url))

print(get_html_from_url(base_url))


def get_themes(url):
    themes = []
    get_html_from_url(url)
    return themes


class Theme:
    def __init__(self, title='', link=''):
        self.title = title
        self.link = link


def serialize(themes=[]):
    with open('themes.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(themes)


def deserialize():
    with open('themes.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))


abc = [
    {1: 'dsfs'},
    {2: 'dmkewmdeomf'}
]

serialize(abc)
deserialize()


class Joke:
    def __init__(self, joke='', link='', tags=()):
        self.joke_text = joke
        self.link = link
        self.meta_tags = tags


def serialize(themes=[]):
    with open('themes.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(themes)


def deserialize():
    with open('themes.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))
