import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://en.wikipedia.org/wiki/Most_common_words_in_English')
soup = BeautifulSoup(page.content, 'html.parser')

tables = soup.select('table')[0:2]
table_1_word_list = tables[0].select('td a')
for an in table_1_word_list:
    print(an.text.lower())
table_2_word_list = tables[1].select('td')
for i in table_2_word_list:
    try:
        int(i.text)
    except ValueError:
        if i.text.strip("\n").strip(" ") != "":
            print(i.text.strip("\n").strip(" ").lower())
