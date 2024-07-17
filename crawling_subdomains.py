import requests

def request(url):
    try:
        return requests.get("https://"+url)
    except requests.exceptions.ConnectionError:
        print("No such subdomains")


target_url = "google.com"
with open("subdomains.txt", "r") as file:
    for line in file:
        word = line.strip() #remove the white space
        test_url = word+ "."+target_url
        response = request(test_url)

        if response:
            print(f"Subdomains {test_url} exists..!!")