# webcrawlers gather info from webpage and find all links
# most popular webcrawler is google search

import requests

from bs4 import BeautifulSoup

def cpbuckingham_spider(max_pages):
    # max pages limitation will be better to test
    page = 1
    while page <= max_pages:
            url = "http://www.amazon.com/s/ref=nb_sb_noss/181-8684667-3708211?url=search-alias%3Daps&field-keywords=fire" + str(page)
            source_code = requests.get(url)
            plain_text =  source_code.text
            soup = BeautifulSoup(plain_text)
            for link in soup.findAll('a', {'class': 'boldRefinementLink'})
                href = link.get('href')

            print(href)
            page += 1

            cpbuckingham_spider(1)
