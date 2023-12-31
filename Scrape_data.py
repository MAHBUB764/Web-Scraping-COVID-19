import requests
from bs4 import BeautifulSoup
import pandas as pd
 
Url="https://www.worldometers.info/coronavirus/"
responce=requests.get(Url)
read=BeautifulSoup(responce.text,"html.parser")
index=read.find('table',{'id':'main_table_countries_today'}).find('tbody').find_all('tr')

country_list=[]

for row in index:
    dic={}
    dic["COUNTRY"]=row.find_all('td')[1].text
    dic["TOTAL_CASES"]=row.find_all('td')[2].text.replace(',','')
    dic["TOTAL_DEATHS"]=row.find_all('td')[4].text.replace(',','')
    dic["TOTAL_TASTS"]=row.find_all('td')[12].text.replace(',','')
    dic["TOTAL_RECOVERED"]=row.find_all('td')[6].text.replace(',','')
    dic["POPULATION"]=row.find_all('td')[14].text.replace(',','')


    country_list.append(dic)
print(country_list)

df=pd.DataFrame(country_list)
df.to_excel('COUNTRY_DATA.xlsx',index=False)
df.to_csv('COUNTRY_DATA.csv',index=False)
 