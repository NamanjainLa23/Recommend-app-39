from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

democlient = MongoClient()
myclient = MongoClient('localhost', 27017)
mydb = myclient["Intern"]
mycol1 = mydb["Scrap1"]
mycol2 = mydb["Scrap2"]


def urlsetter(url):
    if "http" in url:
        return url
    else:
        return "https://news.ycombinator.com/" + url


def update_votes(u, v):
    print("1")
    myquery = {"url": u}
    newvalues = {"$set": {"votes": v}}
    mycol2.update_one(myquery, newvalues)


l1 = []
l2 = []
l3 = []
l4 = []
count = 0

source = requests.get('https://news.ycombinator.com/').text
soup = BeautifulSoup(source, 'lxml')

for tr in soup.find_all('tr', class_='athing'):
    tag = tr.find_all('td', class_='title')[1]

    heading = tag.a.text
    url = tag.a['href']

    if url.endswith('pdf'):  # if non scrapable file found
        l1.append("1")
        continue

    k = urlsetter(url)

    l1.append(k)
    l2.append(heading)
    count = count + 1

for td in soup.find_all('td', class_='subtext'):
    vote = td.span.text
    user = td.a.text

    l3.append(vote)
    l4.append(user)

# adding/updating data
for i in range(count):
    if l1[i] == "1":
        print("Non scrapable file found")
        continue

    x = mycol1.find_one({"url": l1[i]})
    if x:
        update_votes(l1[i], l3[i])
    else:
        print(l1[i])
        print()
        mydict1 = {"url": l1[i], "heading": l2[i]}
        mydict2 = {"url": l1[i], "heading": l2[i],
                   "votes": l3[i], "user": l4[i]}

        x = mycol1.insert_one(mydict1)
        y = mycol2.insert_one(mydict2)
