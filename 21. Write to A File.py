import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.cbc.ca/').text
soup = BeautifulSoup(source, features="html.parser")

#print(soup.prettify())

headline = soup.find('h3')
print(headline.text)

file = open('CBC-Headlines', 'w')

for headline in soup.find_all('h3', class_='headline'):
    print(headline.text)
    file.write(headline.text + '\n')

file.close()