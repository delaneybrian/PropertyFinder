import os
import csv

def write_link_to_file(link):
    cwd = os.getcwd()
    with open(cwd + '/propertylinks.csv','a') as fd:
        fd.write(link + '\n')

def read_all_property_links():
    cwd = os.getcwd()
    with open(cwd + '/propertylinks.csv') as f:
        lines = f.readlines()
        print(lines)

def write_property_to_file(property_dict):
    has_header = True
    cwd = os.getcwd()
    with open(cwd + '/properties.csv', 'r') as f:
        if len(f.readlines()) == 0:
            has_header = False

    print(has_header)
    with open(cwd + '/properties.csv', 'a') as f:
        w = csv.DictWriter(f, property_dict.keys())
        if not has_header:
            w.writeheader()
        w.writerow(property_dict)

dict = {'test': 454, 'wond': 343}

write_property_to_file(dict)