import os

def write_link_to_file(link):
    cwd = os.getcwd()
    with open(cwd + '/propertylinks.csv','a') as fd:
        fd.write(link + '\n')

def read_all_property_links():
    cwd = os.getcwd()
    with open(cwd + '/propertylinks.csv') as f:
        lines = f.readlines()
    return lines

def write_property_to_file(property_dict):
    print(property_dict)
    line = '{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(
              property_dict['price'],
              property_dict['code'],
              property_dict['size'],
              property_dict['address'].replace(',',';'),
              property_dict['county'],
              property_dict['type'],
              property_dict['bedrooms'],
              property_dict['bathrooms'],
              property_dict['date'],
              property_dict['views'],
              property_dict['ber'],
              property_dict['url'],
              property_dict['lat'],
              property_dict['lng'])

    cwd = os.getcwd()
    with open(cwd + '/prpoerties.csv','a') as fd:
        fd.write(line + '\n')