import requests
from bs4 import BeautifulSoup

language = input(
    'Type "en" if you want to translate from French into English, '
    'or "fr" if you want to translate from English into French:\n')
word = input('Type the word you want to translate:\n')

print(f'You chose "{language}" as the language to translate "{word}" to.')

if language == 'en':
    url = f"https://context.reverso.net/translation/french-english/{word}"

elif language == "fr":
    url = f"https://context.reverso.net/translation/english-french/{word}"


r = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})


print(str(r.status_code)+" OK" if r.status_code == 200 else r.status_code)

# created a parse for the page
soup = BeautifulSoup(r.content, 'html.parser')

translation = soup.find_all("a", {'class': 'translation'})

examples = soup.find_all("span", {'class': 'text'})
print("Translations")

print([i.text.strip() for i in translation][1::])
print([i.text.strip() for i in examples])
