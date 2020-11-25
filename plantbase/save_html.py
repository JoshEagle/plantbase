import os

def scrape_to_file(html, path):

    os_command = f"curl {html} > '{path}.html'"
    os.system(os_command)


def main():

    plants = {
        'Chrysanthemum': 'https://www.rhs.org.uk/Plants/178969/i-Chrysanthemum-i-Constable/Details',
        'Campanula': 'https://www.rhs.org.uk/Plants/90552/Campanula-latiloba-Percy-Piper/Details/'
            }

    for key in plants:
        html = plants[key]
        path = key
        scrape_to_file(html, path)


if __name__ == '__main__':
    main()
