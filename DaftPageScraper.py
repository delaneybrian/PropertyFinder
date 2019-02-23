import requests
from bs4 import BeautifulSoup
import re
from FileTools import write_property_to_file
from CoordinateFinder import get_property_cordinates
from time import sleep
from random import randint

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0"
}

def get_page(url):
    sleep(randint(1, 5))
    try:
        r = requests.get(url, headers=headers)
        if(r.status_code == 200):
            return r.content
        else:
            return None
    except Exception as e:
        print("Error Scraping {0} : {1}".format(url, e))

def format_size(value):
    if(value is not None):
        new_string = ''.join(re.findall(r'\d+.\d+', value))
        return new_string

def format_price(value):
    if(value is not None):
        new_string = ''.join(re.findall(r'\d+.\d+', value))
        return new_string.replace(',', '')

def format_string(value):
    if(value is not None):
        return value.strip()

def get_entered_date(soup):

    property_stats = soup.find_all('div', 'PropertyStatistics__iconContainer')
    if(property_stats is not None):
        for property_stat in property_stats:
            if('Entered' in str(property_stat)):
                entered_date = property_stat.find('div', 'PropertyStatistics__iconData')
                if(entered_date is not None):
                    return entered_date.string
    return None

def get_views(soup):

    property_stats = soup.find_all('div', 'PropertyStatistics__iconContainer')
    if (property_stats is not None):
        for property_stat in property_stats:
                if('Property Views' in str(property_stat)):
                    property_views = property_stat.find('div', 'PropertyStatistics__iconData')
                    if(property_views is not None):
                        return property_views.string
    return None

def get_ber_rating(soup):
    ber_section = str(soup.find('div', 'BERDetails__berIconContainer')).upper()

    if(ber_section is not None):
        if ('EXEMPT' in ber_section):
            return 'EXEMPT'
        elif ('A1' in ber_section):
            return 'A1'
        elif ('A2' in ber_section):
            return 'A2'
        elif('A3' in ber_section):
            return 'A3'
        elif ('B1' in ber_section):
            return 'B1'
        elif ('B2' in ber_section):
            return 'B2'
        elif ('B3' in ber_section):
            return 'B3'
        elif ('C1' in ber_section):
            return 'C1'
        elif ('C2' in ber_section):
            return 'C2'
        elif ('C3' in ber_section):
            return 'C3'
        elif ('D1' in ber_section):
            return 'D1'
        elif ('D2' in ber_section):
            return 'D2'
        elif ('E1' in ber_section):
            return 'E1'
        elif ('E2' in ber_section):
            return 'E2'
        elif ('F' in ber_section):
            return 'F'
        elif ('G' in ber_section):
            return 'G'
        else:
            return None
    return None

def get_county(address):

    if(address is None):
        return "UNKNOWN"

    address = address.upper()

    if('ANTRIM' in address):
        return 'ANTRIM'
    elif('ARMAGH' in address):
        return 'ARMAGH'
    elif ('CARLOW' in address):
        return 'CARLOW'
    elif ('CAVAN' in address):
        return 'CAVAN'
    elif ('CLARE' in address):
        return 'CLARE'
    elif ('CORK' in address):
        return 'CORK'
    elif ('DERRY' in address):
        return 'DERRY'
    elif ('DONEGAL' in address):
        return 'DONEGAL'
    elif ('DOWN' in address):
        return 'DOWN'
    elif ('DUBLIN' in address):
        return 'DUBLIN'
    elif ('FERMANAGH' in address):
        return 'FERMANAGH'
    elif ('GALWAY' in address):
        return 'GALWAY'
    elif ('KERRY' in address):
        return 'KERRY'
    elif ('KILDARE' in address):
        return 'KILDARE'
    elif ('KILKENNY' in address):
        return 'KILKENNY'
    elif ('LAOIS' in address):
        return 'LAOIS'
    elif ('LEITRIM' in address):
        return 'LEITRIM'
    elif ('LIMERICK' in address):
        return 'LIMERICK'
    elif ('LONGFORD' in address):
        return 'LONGFORD'
    elif ('LOUTH' in address):
        return 'LOUTH'
    elif ('MAYO' in address):
        return 'MAYO'
    elif ('MEATH' in address):
        return 'MEATH'
    elif ('MONAGHAN' in address):
        return 'MONAGHAN'
    elif ('OFFALY' in address):
        return 'OFFALY'
    elif ('ROSCOMMON' in address):
        return 'ROSCOMMON'
    elif ('SLIGO' in address):
        return 'SLIGO'
    elif ('TIPPERARY' in address):
        return 'TIPPERARY'
    elif ('TYRONE' in address):
        return 'TYRONE'
    elif ('WATERFORD' in address):
        return 'WATERFORD'
    elif ('WESTMEATH' in address):
        return 'WESTMEATH'
    elif ('WEXFORD' in address):
        return 'WEXFORD'
    elif ('WICKLOW' in address):
        return 'WICKLOW'
    else:
        return 'UNKNOWN'

def get_size(soup):
    size = soup.find('div', 'PropertyOverview__propertyOverviewDetails')

    if(size is not None):
        match = re.search('[0-9.d]* m', str(size))
        if match:
            return match.group(0)
    return None

def get_price(soup):
    price_data = soup.find('strong', 'PropertyInformationCommonStyles__costAmountCopy')

    if(price_data is not None):
        return price_data.string
    else:
        return None

def get_address(soup):
    address = soup.find('h1', 'PropertyMainInformation__address')

    if (address is not None):
        return address.string
    else:
        return None

def get_type(soup):
    type = soup.find('div', 'QuickPropertyDetails__propertyType')

    if (type is not None):
        return type.string
    else:
        return None

def get_bedrooms(soup):
    property_details = soup.find_all('div', 'QuickPropertyDetails__iconContainer')

    if(property_details is not None):
        for property_detail in property_details:
            if ('Number of beds' in str(property_detail)):
                bedrooms = property_detail.find('div', 'QuickPropertyDetails__iconCopy')
                if (bedrooms is not None):
                    return bedrooms.string
    return None


def get_bathrooms(soup):
    property_details = soup.find_all('div', 'QuickPropertyDetails__iconContainer')

    if (property_details is not None):
        for property_detail in property_details:
            if ('Number of bathroom' in str(property_detail)):
                bathrooms = property_detail.find('div', 'QuickPropertyDetails__iconCopy--WithBorder')
                if (bathrooms is not None):
                    return bathrooms.string
    return None

def get_code(soup):
    property_code_link = soup.find('a', 'PropertyShortcode__link')

    if (property_code_link is not None):
        match = re.search('https:\/\/www.daft.ie\/([0-9]*)', str(property_code_link.string))
        if match:
            return match.group(1)

def get_property_details(content, url):
    soup = BeautifulSoup(content, features='html.parser')

    price = get_price(soup)
    code = get_code(soup)
    size = get_size(soup)
    address = get_address(soup)
    county = get_county(address)
    type = get_type(soup)
    bedrooms = get_bedrooms(soup)
    bathrooms = get_bathrooms(soup)
    date = get_entered_date(soup)
    views = get_views(soup)
    ber = get_ber_rating(soup)

    return {'price': format_price(price),
            'code': format_string(code),
            'size': format_size(size),
            'address': format_string(address),
            'county': format_string(county),
            'type': format_string(type),
            'bedrooms': format_string(bedrooms),
            'bathrooms': format_string(bathrooms),
            'date': format_string(date),
            'views': format_string(views),
            'ber': format_string(ber),
            'url': url}

def scrape_property_link(url):
    print("Now Scraping {}...".format(url))
    content = get_page(url)
    property = get_property_details(content, url)
    coordinates = get_property_cordinates(property["address"])
    if coordinates is not None:
        property["lat"] = coordinates["lat"]
        property["lng"] = coordinates["lng"]
    else:
        property["lat"] = None
        property["lng"] = None
    write_property_to_file(property)
