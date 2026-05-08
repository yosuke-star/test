import requests, bs4

r = requests.get('https://nostarch.com')
r.raise_for_status()
no_starch_soup = bs4.BeautifulSoup(r.text, 'html.parser')
print(type(no_starch_soup))