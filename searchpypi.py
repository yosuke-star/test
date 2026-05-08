import requests, bs4, sys, webbrowser

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
r = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]), headers=headers)

#r = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
r.raise_for_status()

soup = bs4.BeautifulSoup(r.text, 'html.parser')
print(soup.prettify()[:3000])
link_elems = soup.select('.package-snippet__name')
print(len(link_elems))

num_open = min(5, len(link_elems))
for i in range(num_open):
    url_to_open = 'https://pypi.org' + link_elems[i].get('href')
    print('Opening', url_to_open)
    webbrowser.open(url_to_open)