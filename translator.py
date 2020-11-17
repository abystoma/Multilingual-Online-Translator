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

translations = [i.text.strip()
                for i in soup.find_all("a", {'class': 'translation'})][1::]

english_examples = [i.text.strip()
                    for i in soup.find_all("div", {'class': 'src ltr'})]

french_examples = [i.text.strip()
                   for i in soup.find_all("div", {'class': 'trg ltr'})]
print("Context examples:")
print()
print("French Translations:")

for translation in translations[:5]:
    print(translation)

print()
print("French Examples:")

for en, fr in zip(english_examples[:5], french_examples[:5]):
    print(en+":\n"+fr)
    print()
