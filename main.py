from DaftPageScraper import scrape_property_link
from DaftLinkScraper import start_link_scrape
from FileTools import read_all_property_links

property_links = start_link_scrape()
#property_links = read_all_property_links()

#for property_link in property_links:
    #scrape_property_link(property_link.rstrip())