  ""
import sqlite3 as sq
import requests
import selectorlib
import datetime as dt
conn=sq.connect("price.db")
cursor=conn.cursor()
conn.commit()

search=input("enter the product url :")
url=f"{search}"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
def scrape(url):
    response=requests.get(url,headers=headers)
    source=response.text
    return source
def extract(source):
    extractor=selectorlib.Extractor.from_yaml_file("get.yaml")
    date=dt.datetime.now()
    print(date)
    value=extractor.extract(source)

    return value["price"]
def store_price():
    price=extract(source)
    date=dt.datetime.now()
    "INSERT INTO PRICE VALUES"



if __name__=="__main__":
    source=scrape(url)
    extract=extract(source)
"