from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

democlient = MongoClient()
myclient = MongoClient('localhost', 27017)
mydb = myclient["Intern"]
mycol1 = mydb["Scrap1"]
mycol2 = mydb["Scrap2"]

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

    l1.append(heading)
    l2.append(url)
    count = count + 1

for td in soup.find_all('td', class_='subtext'):
    vote = td.span.text
    user = td.a.text

    l3.append(vote)
    l4.append(user)

for i in range(count):
    x = mycol1.find_one({"url": l2[i]})
    if x:
        print("1")
        myquery = {"url": l2[i]}
        newvalues = {"$set": {"votes": l3[i]}}
        mycol2.update_one(myquery, newvalues)
        # update votes
    else:
        print(l2[i])
        mydict1 = {"url": l2[i], "heading": l1[i]}
        mydict2 = {"url": l2[i], "heading": l1[i],
                   "votes": l3[i], "user": l4[i]}
#
        x = mycol1.insert_one(mydict1)
        y = mycol2.insert_one(mydict2)
#
#    #    print(l1[i])
#    #    print(l2[i])
#    #    print(l3[i])
    #     print(l4[i])
