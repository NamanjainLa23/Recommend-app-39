from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import csv

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

csv_file = open('Scraped_data.csv', 'a')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['url', 'heading', 'user', 'vote'])

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
        continue
    else:
        print(x)
    #    mydict1 = {"url": l2[i], "heading": l1[i]}
    #    mydict2 = {"url": l2[i], "heading": l1[i],
    #               "votes": l3[i], "user": l4[i]}
#
#    #    x = mycol1.insert_one(mydict1)
#    #    y = mycol2.insert_one(mydict2)
#
#    #    csv_writer.writerow((l1[i], l2[i], l3[i], l4[i]))
#    #    print(l1[i])
#    #    print(l2[i])
#    #    print(l3[i])
    #    print()

# csv_file.close()
