from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

democlient = MongoClient()
myclient = MongoClient('localhost', 27017)
mydb = myclient["Intern"]
mycol1 = mydb["Scrap1"]
mycol2 = mydb["Scrap2"]
mycol3 = mydb["Scrap3"]

desc_link = list(mycol1.find({}, {"_id": 0, "url": 1}))
for link in desc_link:
    for k in link.values():
        source = requests.get(k).text
        soup = BeautifulSoup(source, 'lxml')

        desc = ""
        for p in soup.find_all('p'):
            desc = desc + p.text
            desc.lstrip(" ")
            desc.rstrip(" ")
            desc.lstrip("\n")
            desc.rstrip("\n")

        if desc:
            mydict3 = {"url": k, "desc": desc}
            x = mycol3.insert_one(mydict3)
        else:
            mydict3 = {"url": k, "desc": "No Description in given page"}
            x = mycol3.insert_one(mydict3)
