from bs4 import BeautifulSoup
import requests
import pandas as pd

years = [1930,1934,1938,1950,
        1954,1958,1962,1966,
        1970,1974,1978,1982,
        1986,1990,1994,1998,
        2002,2006,2010,2014,2018] 

def get_matches(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    response = requests.get(web)
    content =response.text
    soup = BeautifulSoup(content,'lxml')

    matches = soup.find_all('div',class_='footballbox')

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find('th', class_='fhome').get_text())
        score.append(match.find('th',class_='fscore').get_text())
        away.append(match.find('th',class_='faway').get_text())
        

    dict_soccer = {'home': home, 'score': score, 'away': away}
    df_soccer = pd.DataFrame(dict_soccer)
    df_soccer['year'] = year
    return df_soccer

def get_matches_qatar(year):
    web = f'https://web.archive.org/web/20221115040351/https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    response = requests.get(web)
    content =response.text
    soup = BeautifulSoup(content,'lxml')

    matches = soup.find_all('div',class_='footballbox')
    
    home = []
    score = []
    away = []
    
    for match in matches:
        home.append(match.find('th', class_='fhome').get_text())
        score.append(match.find('th',class_='fscore').get_text())
        away.append(match.find('th',class_='faway').get_text())
        

    dict_soccer = {'home': home, 'score': score, 'away': away}
    df_soccer = pd.DataFrame(dict_soccer)
    df_soccer['year'] = year
    return df_soccer

#historial_data
fifa=[get_matches(year) for year in years]
df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv('fifa_worldcup_historial_data', index=False)



df_fixture = get_matches_qatar('2022')
df_fixture.to_csv('fifa_worldcup_fixture_data', index=False)
#print(get_matches(2018))

print(df_fixture)