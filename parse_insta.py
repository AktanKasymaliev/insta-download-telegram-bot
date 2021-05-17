import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup as bs
from time import sleep
import datetime
import fake_useragent


def request(url, head=None):
    r = requests.get(url, headers=head, auth=HTTPBasicAuth("*", "*"))
    sleep(2)
    return r

def write_file(file_name):
    file_format = file_name.split('/')[-1].split('?')[0].split('.')[-1]
    created_name = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    with open(f"{created_name}.{file_format}", 'wb') as file:
        file.write(request(file_name).content)

while True:
    fake_headers=fake_useragent.UserAgent().random
    head = {'user-agent': fake_headers}
    link = input("Link: ")
    response = request(link, head)
    soup = bs(response.text, 'html.parser')
    if soup.find_all('meta', {'property':'og:video'}):
        metaTag = soup.find_all('meta', {'property':'og:video'})
    else:
        metaTag = soup.find_all('meta', {'property':'og:image'})
    write_file(metaTag[0]["content"])
