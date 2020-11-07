import requests #access url and pull out data
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.de/LABISTS-Ultimatives-Aus-Schaltnetzteil-K%C3%BChlk%C3%B6rper-HDMI-Kabel/dp/B07W7Q6ZC9/ref=sr_1_2_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3E9WFDVPWHQJY&dchild=1&keywords=raspberry+pi+4&qid=1604779663&quartzVehicle=812-409&replacementKeywords=raspberry+pi&sprefix=rasp%2Caps%2C182&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNFJZWThFRFVNMlRVJmVuY3J5cHRlZElkPUEwNzYxNDE3MlMxRDVKOU0zRTBTUCZlbmNyeXB0ZWRBZElkPUEwMjU2MDIyM0NKQlVJVVo0M0VWOCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers) #returns all data from the website

    soup = BeautifulSoup(page.content, 'html.parser') #parses it -> You can then pull anything with f12

    #title = soup.find(id = "productTitle").get_text() #-> print(title.strip()) strip to not get space
    price = float(soup.find(id = "price_inside_buybox").get_text()[:4])
    #converted_price = float(price[:3])

    if price < 100:
        send_mail()

    print(price)
    #print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('alex.spiesberger@gmail.com', 'oegnyvahinoourwu')

    subject = 'Price fell down!'
    body = 'check the amazon link: https://www.amazon.de/LABISTS-Ultimatives-Aus-Schaltnetzteil-K%C3%BChlk%C3%B6rper-HDMI-Kabel/dp/B07W7Q6ZC9/ref=sr_1_2_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3E9WFDVPWHQJY&dchild=1&keywords=raspberry+pi+4&qid=1604779663&quartzVehicle=812-409&replacementKeywords=raspberry+pi&sprefix=rasp%2Caps%2C182&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNFJZWThFRFVNMlRVJmVuY3J5cHRlZElkPUEwNzYxNDE3MlMxRDVKOU0zRTBTUCZlbmNyeXB0ZWRBZElkPUEwMjU2MDIyM0NKQlVJVVo0M0VWOCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'alex.spiesberger@gmail.com',
        'alex.spiesberger@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()


while True:
    check_price()
    time.sleep((60*60)*48) #checks every 2 days