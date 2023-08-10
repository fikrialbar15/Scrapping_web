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
    
#kolom data
print("Kolom Database")    
print(df)

#merubah kolom rank menjadi integer
df['Rank'] = df['Rank'].astype(int)

print("Merubah kolom rank")
print(df)

#merubah kolom Revenue (USD millions), menghilangkan koma dan merubah menjadi integer
df['Revenue (USD millions)'] = df['Revenue (USD millions)'].str.replace(",", "").astype(int)

print("kolom Revenue(USD millions) di ubah")
print(df)

#Merubah kolom Revenue growth menjadi float dan menghapus %
df['Revenue growth'] = df['Revenue growth'].str.replace("%", "").astype(float)

print("Kolom Revenue growth di ubah")
print(df)

#merubah kolom Employees, menghapus koma dan merubah menjadi integer
df['Employees'] = df['Employees'].str.replace(",", "").astype(int)

print("Kolom Employees di ubah")
print(df)

#memasukan data Scrapping ke dalam database di pgadmin
engine = create_engine(
    f"postgresql://postgres:151515@localhost:5432/postgres")

#companies ini nama tabel yang nantinya ada di pgadmin
df.to_sql('companies_3', con=engine, if_exists="replace", index=False)

#untuk menyimpan file dalam csv dan excel
#df.to_csv(r'D:\PKL\scrapping web\Percobaan_Scraping_web_Companies.csv', index = False)
