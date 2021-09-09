from bs4 import BeautifulSoup
import requests

html = requests.get(
    "https://www.climatempo.com.br/previsao-do-tempo/cidade/256/joaopessoa-pb").content

soup = BeautifulSoup(html, 'html.parser')

resume = soup.find(class_='-gray -line-height-24 _center')
tempMin = soup.find(id='min-temp-1')
tempMax = soup.find(id='max-temp-1')

print(f'Resumo \n {resume.text}\n')
print(' Temp. Mínima ' + tempMin.string)
print(' Temp. Máxima ' + tempMax.string)
