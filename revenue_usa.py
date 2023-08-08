from bs4 import BeautifulSoup
import requests
from sqlalchemy import create_engine
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

soup.find_all('table')[1]

soup.find_all('table', class_ = 'wikitable sortable')

table = soup.find_all('table')[1]

world_titles = table.find_all('th')

#untuk menampilkan judul
world_table_titles = [title.text.strip() for title in world_titles]

#membuat judul data frame
df = pd.DataFrame(columns = world_table_titles)

column_data = table.find_all('tr')

#mengambil isi database untuk di masukin ke dalam kolom
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data
    
print(df)

#untuk menyimpan file dalam csv dan excel
#df.to_csv(r'D:\PKL\scrapping web\Percobaan_Scraping_web_Companies.csv', index = False)
