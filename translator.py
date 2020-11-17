import requests
from bs4 import BeautifulSoup

languages = [None,
             "Arabic",
             "German",
             "English",
             "Spanish",
             "French",
             "Hebrew",
             "Japanese",
             "Dutch",
             "Polish",
             "Portuguese",
             "Romanian",
             "Russian",
             "Turkish"]


print("""Hello, you're welcome to the translator. Translator supports: 
1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish""")

src_lang = int(input("Type the number of your language: "))
lang_in = languages[src_lang].lower()
trg_lang = int(input("Type the number of language you want to translate to: "))
lang_out = languages[trg_lang].lower()

word = input("Type the word you want to translate: ")

url = f"https://context.reverso.net/translation/{lang_in}-{lang_out}/{word}"


r = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})

# created a parse for the page
soup = BeautifulSoup(r.content, 'html.parser')

translations = [i.text.strip()
                for i in soup.find_all("a", {'class': 'translation'})][1::]

src_examples = [i.text.strip()
                for i in soup.find_all("div", {'class': 'src ltr'})]

trg_examples = [i.text.strip()
                for i in soup.find_all("div", {'class': 'trg ltr'})]
print()
print(f"{lang_out.title()} Translations:")

for translation in translations[:5]:
    print(translation)

print()
print(f"{lang_out.title()} Examples:")

for src, trg in zip(src_examples[:5], trg_examples[:5]):
    print(src+":\n"+trg)
    print()
