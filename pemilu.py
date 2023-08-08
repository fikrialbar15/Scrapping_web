from bs4 import BeautifulSoup
import requests

import pandas as pd

url = 'https://id.wikipedia.org/wiki/Pemilihan_umum_legislatif_Indonesia_2024#Partai_politik_nasional'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

soup.find_all('table')

soup.find_all('table', class_ = 'wikitable')

table = soup.find_all('table', class_ = 'wikitable')[4]

world_titles = table.find_all('th')

world_table_titles = [title.text.strip() for title in world_titles if title.text.strip() and not title.text.strip().isdigit() ]

df = pd.DataFrame(columns = world_table_titles)

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data
    
print(df)

#untuk menyimpan file dalam csv
#df.to_csv(r'D:\PKL\scrapping web\Percobaan_Scraping_web_Companies.csv', index = False)