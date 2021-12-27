import requests
from bs4 import BeautifulSoup

url = "https://www.songshanculturalpark.org/Exhibition.aspx?ID=637a3ee3-07ee-471e-b573-c03447e1d7dc"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

print(soup)

