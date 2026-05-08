import bs4

index_file = open('index.html')
index_soup = bs4.BeautifulSoup(index_file, 'html.parser')

element = index_soup.select('p')
print(element)
