import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


def parse(html):

    soup = BeautifulSoup(html, 'html.parser')

    titles = []
    paras = []

    plant_name = soup.find('h1', class_='Plant-formated-Name').text.strip()
    titles.append('Sepcies')
    paras.append(plant_name)

    summary_block = soup.find('ul', class_='clr', id='plant_details_desc')
    summary_ids = [
        'ctl00_ctl00_ctl00_plcMainContent_plcMainContent_plcMainContent_PlantDetail1_Li15',
        'ctl00_ctl00_ctl00_plcMainContent_plcMainContent_plcMainContent_PlantDetail1_Li2',
        'ctl00_ctl00_ctl00_plcMainContent_plcMainContent_plcMainContent_PlantDetail1_Li3'
            ]
    details = []
    for detail_id in detail_ids:
        details.append(detail_block.find('li', id=detail_id))
    for part in summary:
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

    return


def scrape_from_file(plant):

    os_command = f"curl {plant} > f'plant.html'"
    os.system(os_command)
    file = f'{plant}.html'
    return open(file)


def main():

    plants = {
        'Narcissus': 'https://www.rhs.org.uk/Plants/45358/Narcissus-Trena-(6)/Details/',
        'Campanula': 'https://www.rhs.org.uk/Plants/90552/Campanula-latiloba-Percy-Piper/Details/'
            }

    result = {}

    for key, value in plants.items():
        site_name = plants.key
        site_url = plants.value
        plant_details = parse(scrape_from_file(plant))


    return plant_details


if __name__ == '__main__':
    main()


    # df = pd.DataFrame([paras], columns=titles)

    # df.to_csv('plants.csv')
