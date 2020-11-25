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

    plant_info_df.to_csv('plant_info.csv')


if __name__ == '__main__':
    main()
