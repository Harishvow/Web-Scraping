import smtplib, ssl

import sqlite3 as sq


import requests
import selectorlib
import datetime as dt
conn=sq.connect("price.db")
cursor=conn.cursor()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
def scrape(url):
    response=requests.get(url,headers=headers)
    source=response.text
    return source
def extract(source):
    extractor=selectorlib.Extractor.from_yaml_file("get.yaml")
    value=extractor.extract(source)["price"]




    return value

def store_price(rup):
    price=rup
    date=dt.datetime.now().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO PRICE (DATE,PRICE) VALUES(?,?)",(date,price))
    conn.commit()

    return
def get_price():
        cursor.execute("SELECT DATE, PRICE FROM PRICE WHERE DATE = ?")
        result = cursor.fetchone()
        return result
def send_email(receiver,message):
    host = "smtp.gmail.com"
    port = 465

    username = "harisharish982005@gmail.com"
    password = "edyhxxieeuietyua"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)




