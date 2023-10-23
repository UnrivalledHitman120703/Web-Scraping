# Web scraping using python
# Name = Indrajeet Mondal; Date = 24th October 2023
# SourceCode

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.find_all('div'))