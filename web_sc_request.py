import requests

r = requests.get('https://automatetheboringstuff.com/files/rj.txt')
r.raise_for_status()

play_file = open('RomeoAndJuliet.txt', 'wb')

for chunk in r.iter_content(100000):
    play_file.write(chunk)

play_file.close()