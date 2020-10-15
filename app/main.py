import argparse
import re
import requests

parser = argparse.ArgumentParser(
    description='Take MAC Address as input, API Key as well if required')

parser.add_argument("-mac", "--macaddress", type=str, action="store", dest="mac", default='44:38:39:ff:ef:57', help="Please provide a valid MAC address")
parser.add_argument("-apikey", "--apikey", type=str, action="store", dest="apikey", default='at_0lsz0Ny9kHRc3oYVzQ7b7Z74NkwxD', help="Please provide a valid API Key")

results = parser.parse_args()
mac = results.mac
apikey = results.apikey

if re.match("[0-9a-f]{2}([-:.]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
    # api-endpoint 
    url = f"https://api.macaddress.io/v1?apiKey={apikey}&output=json&search={mac}"

    headers = {'Accept': 'json'}
    
    # sending get request and saving the response as response object 
    response = requests.get(url, headers=headers)
    
    # extracting data in json format 
    data = response.json()

    company_name = data['vendorDetails']['companyName']
    print("Company name associated with this mac address:\n",company_name)

else:
    print("invalid mac address format")