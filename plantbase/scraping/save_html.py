import os

def scrape_to_file(html, path):

    os_command = f"curl {html} > '{path}.html'"
    os.system(os_command)


def main():

    plants = {
        'Daffodils': 'https://www.rhs.org.uk/Plants/96695/Narcissus-cantabricus-subsp-cantabricus-var-foliosus-(13)/Details',
        'Campanula': 'https://www.rhs.org.uk/Plants/90552/Campanula-latiloba-Percy-Piper/Details/',
        'Verbascum': 'https://www.rhs.org.uk/Plants/238917/i-Verbascum-i-Rosie/Details',
        'Crataegus': 'https://www.rhs.org.uk/Plants/113247/i-Crataegus-monogyna-i-Ferox/Details',
        'Geranium': 'https://www.rhs.org.uk/Plants/272623/i-Geranium-i-Melinda/Details',
        'Ophrys': 'https://www.rhs.org.uk/Plants/11841/i-Ophrys-apifera-i/Details',
        'Hyacinth': 'https://www.rhs.org.uk/Plants/2403/i-Brimeura-amethystina-i/Details',
        'Hydrangea': 'https://www.rhs.org.uk/Plants/8951/i-Hydrangea-seemannii-i/Details',
        'Iris': 'https://www.rhs.org.uk/Plants/378994/i-Iris-i-Sulphureux/Details',
        'Jasmine': 'https://www.rhs.org.uk/Plants/9454/i-Jasminum-officinale-i/Details',
        'Lavender': 'https://www.rhs.org.uk/Plants/225995/i-Lavandula-i-Pukehou/Details',
        'Rhododendron': 'https://www.rhs.org.uk/Plants/51454/i-Rhododendron-i-Schneekrone/Details',
        'Roses': 'https://www.rhs.org.uk/Plants/90968/i-Rosa-i-FONT-FACE-Times-New-Roman-Mary-Rose-FONT-Ausmary-(S)/Details',
        'Snowdrops': 'https://www.rhs.org.uk/Plants/1261/i-Anemone-sylvestris-i/Details',
        'Tulip': 'https://www.rhs.org.uk/Plants/258038/i-Tulipa-i-Belicia-(2)/Details',
        'Wisteria': 'https://www.rhs.org.uk/Plants/19123/i-Wisteria-floribunda-i/Details'
            }

    for key in plants:
        html = plants[key]
        path = key
        scrape_to_file(html, path)


if __name__ == '__main__':
    main()
