import requests
from bs4 import BeautifulSoup
import smtplib
import time

#input the url to scrap daa from 
url = 'https://www.jumia.co.ke/redmi-note-8-6.3-fhd-4gb-ram-64gb-48mp-4g-black-xiaomi-mpg224066.html'

headers = {
    'User_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
}
def scrapp():

    res = requests.get(url , headers=headers)
    soup = BeautifulSoup(res.content,'html.parser')

    # print(soup.prettify())
    title = soup.find(attrs='-fs20 -pts -pbxs').get_text()
    price = soup.find(attrs="-b -ltr -tal -fs24").get_text()
    converted_price = float(price[4:].replace(",",""))

    print(title,converted_price)
    if converted_price < 17000:
        send_mail()
    elif converted_price ==18999:
        send_mail()

# function to send mail
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("kimfreelance5@gmail.com", "plldokwiaguoxamw")

    subject = "Hey price fell!"
    body = "Check out the link below for the new price update https://www.jumia.co.ke/redmi-note-8-6.3-fhd-4gb-ram-64gb-48mp-4g-black-xiaomi-mpg224066.html"

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'kimfreelance5@gmail.com',
        'nickngeno1@gmail.com',
        msg
    )
    print("Email has been sent!")
    server.quit()

while (True):
    scrapp()
    time.sleep(3600)
