import requests

url = 'www.facebook.com'

try:
    get_response = requests.get("https://"+url)
    print(get_response)
except requests.exceptions.ConnectionError:
    print("There is no website")