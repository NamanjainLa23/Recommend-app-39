from bs4 import BeautifulSoup
import requests
import re
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

        if desc:
            pass
        else:
            desc = "No Description in given page"
            pass

        desc1 = re.sub(r'\n', ' ', desc)
        desc2 = re.sub(r'\s+', ' ', desc1)
        desc3 = re.sub(r'â', "'", desc2)
        desc4 = re.sub(r'â', "'", desc3)
        desc5 = re.sub(r'â¢', ".", desc4)

        x = mycol3.find_one({"url": k})
        if x:
            print("skipped")
            continue
        else:
            print(desc5)
            mydict3 = {"url": k, "desc": desc5}
            x = mycol3.insert_one(mydict3)
