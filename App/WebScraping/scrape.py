from bs4 import BeautifulSoup
import requests

source = requests.get('https://news.ycombinator.com/').text
soup = BeautifulSoup(source, 'lxml')

for tr in soup.find_all('tr', class_='athing'):
    tag = tr.find_all('td', class_='title')[1]

    heading = tag.a.text
    url = tag.a['href']

    print(heading)
    print(url, end="")

    td = soup.find('td', class_='subtext').text
    store = td.split(" ")

    vote = store[0] + " " + store[1]
    user = store[3]

    print(vote)
    print(user)
    print()
