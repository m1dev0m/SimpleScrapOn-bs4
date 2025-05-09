#My Simple Web Scraping Project in 3 Minutes

import requests
from bs4 import BeautifulSoup
import csv


url = 'https://senate.parlam.kz/ru-RU/about/deputies'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
cards = soup.find_all('a', class_='person-card')


with open('deputies.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['ФИО', 'Должность'])
    for card in cards:
        name_tag = card.find('div', class_='person-card--full-name')
        name = name_tag.text.strip() if name_tag else 'Нет имени'
        position_tag = card.find('div', class_='person-card--position')
        position = position_tag.text.strip() if position_tag else 'Нет должности'
        writer.writerow([name, position])
