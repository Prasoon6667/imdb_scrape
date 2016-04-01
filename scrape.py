import requests
from bs4 import BeautifulSoup
import codecs



url = 'http://www.imdb.com/chart/top?ref_=nv_mv_250_6'
response = requests.get(url)
html = response.content

fd = open('scrapeText.txt', 'w+')

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'class' : 'lister-list'})


for row in table.findAll('tr'):
    cells = row.findAll('td')
    name = cells[1].find('a')
    rating = cells[2].find('strong')
    writeToFile = name.find(text = True) + " rating is " + rating.find(text = True)
    fd.write(writeToFile)
    
    
    
        
        

