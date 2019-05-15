import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture').text
soup = BeautifulSoup(source, features="html.parser")

#print(soup.prettify())

#article = soup.find('article')
#print(article.prettify())
#headline = article.h1.text
#print(headline)

#or story in soup.find_all('p'):
    #print(story)

story = soup.find('section', class_='content-section')
sent = story.p.text
print(story)
