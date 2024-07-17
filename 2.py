import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = input("Enter a website for extraction process:")

response = requests.get("http://"+url)

data = response.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    test_link = link.get('href')
    link = urljoin(url, test_link)
    print(link)