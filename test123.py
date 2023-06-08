from bs4 import BeautifulSoup
import requests


url = 'https://www.genie.co.kr/chart/top200'
header_info = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'}
page = requests.get(url, headers=header_info)
page = page.text

soup = BeautifulSoup(page, 'html.parser')

top50_songs = soup.find_all('a', class_='title ellipsis')


top50_songs_list = list()

for each_data in top50_songs:
    song_name = each_data.text
    song_name = song_name.strip()
    top50_songs_list.append(song_name)

print(top50_songs_list)
