from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

path = "C:\\Users\\sebas\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

service = Service(executable_path=path)

# Extraer la data que queremos de la página web
driver = webdriver.Chrome(service=service)

def get_missing_data(year):

# Proporcionar la URL como argumento al método get()
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    driver.get(web)

    matches= driver.find_elements(by='xpath', value= '//tr[@itemprop="name"]')

    home =[]
    score=[]
    away= []

    for match in matches:
        home.append(match.find_element(by='xpath',value='./th[1]').text)
        score.append(match.find_element(by='xpath',value='./th[2]').text)
        away.append(match.find_element(by='xpath',value='./th[3]').text)
    
    
    dict_soccer = {'home': home, 'score':score, 'away':away}
    df_soccer = pd.DataFrame(dict_soccer)
    df_soccer['year'] = year
    time.sleep(2)
    return df_soccer

years = [1930,1934,1938,1950,
        1954,1958,1962,1966,
        1970,1974,1978,1982,
        1986,1990,1994,1998,
        2002,2006,2010,2014,2018] 

fifa = [get_missing_data(year) for year in years]
driver.quit()
df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv('test_fifa.csv', index=False)