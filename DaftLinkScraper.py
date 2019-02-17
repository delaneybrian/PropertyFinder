import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0"
}

start_url = "https://www.daft.ie/ireland/property-for-sale"

base_address = "https://www.daft.ie"

def get_page(url):
    sleep(randint(1, 10))
    try:
        r = requests.get(url, headers=headers)
        if(r.status_code == 200):
            return r.content
        else:
            return None
    except Exception as e:
        print("Error Scraping {0} : {1}".format(url, e))

def get_all_property_links_for_page(soup):
    link_soup = soup.find_all('a', 'PropertyImage__mainImageBigLink')

    if(link_soup is not None):
        links = []
        for link in link_soup:
            links.append(base_address + link['href'])
    return links

def get_next_link(soup):
    next_page_list = soup.find('li', 'next_page')

    if(next_page_list is not None):
        next_page_link = next_page_list.find('a')
        if(next_page_link is not None):
            return (base_address + next_page_link['href'])

url = start_url
links = []
itrs = 0

while(True):
    content = get_page(url)
    soup = BeautifulSoup(content, features='html.parser')
    property_links = get_all_property_links_for_page(soup)
    for property_link in property_links:
        links.append(property_link)
    url = get_next_link(soup)
    if(property_links is None or len(property_links) == 0):
        break
    itrs += 1
    if(itrs > 2):
        break
