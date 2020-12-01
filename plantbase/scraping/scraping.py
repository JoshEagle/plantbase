import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


def parse(file):

    soup = BeautifulSoup(open(file), 'html.parser')

    titles = []
    paras = []

    plant_name = soup.find('h1', class_='Plant-formated-Name').text.strip()
    titles.append('Species')
    paras.append(plant_name)

    detail_block = soup.find('ul', class_='clr', id='plant_details_desc')
    detail_ids = [
        'ctl00_ctl00_ctl00_plcMainContent_plcMainContent_plcMainContent_PlantDetail1_Li15',
        'ctl00_ctl00_ctl00_plcMainContent_plcMainContent_plcMainContent_PlantDetail1_Li2',
        'ctl00_ctl00_ctl00_plcMainContent_plcMainContent_plcMainContent_PlantDetail1_Li3'
            ]
    details = []
    for detail_id in detail_ids:
        details.append(detail_block.find('li', id=detail_id))
    for part in details:
        title = part.find('strong').text
        para = part.text.replace(title,'').strip()
        titles.append(title)
        paras.append(para)

    titles.insert(0, 'Genus name')
    paras.insert(0, paras[2].split()[0])

    characteristics = soup.find('div', class_='grid g3 char').find_all('li')
    for i in range(2):
        title = characteristics[i].strong.text.strip()
        para = characteristics[i].text.replace(characteristics[0].strong.text,'').strip()
        titles.append(title)
        paras.append(para)
    for li in characteristics[2].find_all('li'):
        if characteristics[2].find_all('p')[2].text in li.text:
            title = characteristics[2].h5.text.strip()
            para = li.text
            titles.append(title)
            paras.append(para)

    sunlight = soup.find('div', class_='grid sun g3')
    titles.append('Sunlight')
    paras.append(sunlight.find_all('li')[0].text.strip())
    for i in range(1,3):
        if type(sunlight)=='bs4.element.Tag':
            title = sunlight.find_all('li')[i].strong.text.strip()
            para = sunlight.find_all('li')[i].text.replace(title,'').strip()
            titles.append(title)
            paras.append(para)

    soil = soup.find('div', class_='grid soil g3')
    for i in range(3):
        title = soil.find_all('p')[len(soil.find_all('p'))-3+i].strong.text.strip()
        para = soil.find_all('p')[len(soil.find_all('p'))-3+i].text.replace(title,'').strip()
        titles.append(title)
        paras.append(para)

    size = soup.find('div', class_='grid size g3')
    for i in range(3):
        title = size.find_all('p')[i].strong.text.strip()
        para = size.find_all('p')[i].text.replace(title,'').strip()
        titles.append(title)
        paras.append(para)

    how_to_grow = soup.find('div', class_='how-to').find_all('p')
    for part in how_to_grow:
        title = part.find('strong').text
        para = part.text.replace(title,'').strip()
        titles.append(title)
        paras.append(para)

    how_to_care = soup.find('div',
            class_='how-to how-to-double-margin').find_all('p')
    for part in how_to_care:
        title = part.find('strong').text
        para = part.text.replace(title,'').strip()
        titles.append(title)
        paras.append(para)

    return dict(zip(titles, paras))


def main():

    plant_info = []


    for file in os.listdir('.'):
        if file.endswith('.html'):
            plant_info.append(parse(file))

    plant_info_df = pd.DataFrame(plant_info)

    plant_info_df.to_csv('plant_info_wk2.csv')


if __name__ == '__main__':
    main()
