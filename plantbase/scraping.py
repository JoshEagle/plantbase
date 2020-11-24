import requests
from bs4 import BeautifulSoup
import pandas as pd

plants = {
    'Daffodils': '45358/Narcissus-Trena-(6)/Details',
    'Campanula': '90552/Campanula-latiloba-Percy-Piper/Details',
    # 'Verbascum': ,
    # 'Crataegus': ,
    # 'Geranium': ,
    # 'Ophrys': ,
    # 'Hyacinth': ,
    # 'Hydrangea': ,
    # 'Iris': ,
    # 'Jasmine': ,
    # 'Lavender': ,
    # 'Rhododendron': ,
    # 'Roses': ,
    # 'Snowdrops': ,
    # 'Tulip': ,
    # 'Wisteria':
}



for plant in plants.values():
    html = 'https://www.rhs.org.uk/Plants/{plant}'
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


    df = pd.DataFrame([paras], columns=titles)

    df.to_csv('plants.csv')
