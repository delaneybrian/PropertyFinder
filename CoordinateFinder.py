import requests

api_key =  "AIzaSyAQvz129R-O32SXWtcDrPthPZIWx0lmzO0"
address = "31 Shannon Haven, Dromod, Co. Leitrim"


def get_content_from_api(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}".format(address, api_key)
    response = requests.get(url)
    if(response.status_code == 200):
        if(response.content != None):
            return response

def extract_lat_lng_data(response):
    json = response.json()
    if ('results' in json):
        results = json['results']
        if len(results) == 1:
            result = results[0]
            if ('geometry' in result):
                geometry = result["geometry"]
                if ('location' in geometry):
                    lat = geometry['location']['lat']
                    lng = geometry['location']['lng']
                    return {'lat': lat,
                            'lng': lng}

def ensure_is_ireland(info_dict):
    lat = info_dict['lat']
    lng = info_dict['lng']

    if(lat > 56 or lat < 50):
        return False
    if(lng > -5 or lng < -11):
        return False
    return True


content = get_content_from_api(address)
info_dict = extract_lat_lng_data(content)
print(ensure_is_ireland(info_dict))

print(info_dict)