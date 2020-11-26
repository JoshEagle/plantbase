import os

def scrape_to_file(html, path):

    os_command = f"curl {html} > '{path}.html'"
    os.system(os_command)


def main():

    plants = {
        'Campanula': 'https://www.rhs.org.uk/Plants/90552/Campanula-latiloba-Percy-Piper/Details/',
        'Crataegus': 'https://www.rhs.org.uk/Plants/113247/i-Crataegus-monogyna-i-Ferox/Details',
        'Geranium': 'https://www.rhs.org.uk/Plants/272623/i-Geranium-i-Melinda/Details',
        'Narcissus': 'https://www.rhs.org.uk/Plants/96695/Narcissus-cantabricus-subsp-cantabricus-var-foliosus-\(13\)/Details',
        'Ophrys': 'https://www.rhs.org.uk/Plants/11841/i-Ophrys-apifera-i/Details',
        'Rosa': 'https://www.rhs.org.uk/Plants/90968/i-Rosa-i-FONT-FACE-Times-New-Roman-Mary-Rose-FONT-Ausmary-\(S\)/Details',
        'Verbascum': 'https://www.rhs.org.uk/Plants/238917/i-Verbascum-i-Rosie/Details',
        'Iris': 'https://www.rhs.org.uk/Plants/378994/i-Iris-i-Sulphureux/Details',
        'Allium': 'https://www.rhs.org.uk/Plants/175896/i-Allium-i-Universe/Details',
        'Ajuga': 'https://www.rhs.org.uk/Plants/30302/i-Ajuga-pyramidalis-i/Details',
        'Veronica': 'https://www.rhs.org.uk/Plants/18837/i-Veronica-gentianoides-i/Details',
        'Gentiana': 'https://www.rhs.org.uk/Plants/201592/i-Gentiana-i-Iona-sup-\(PBR\)-sup/Details',
        'Viola': 'https://www.rhs.org.uk/Plants/371128/i-Viola-i-Carousel/Details',
        'Malva': 'https://www.rhs.org.uk/Plants/10797/i-Malva-moschata-i/Details',
        'Cirsium': 'https://www.rhs.org.uk/Plants/210825/i-Cirsium-i-Mount-Etna/Details',
        'Trifolium': 'https://www.rhs.org.uk/Plants/18368/i-Trifolium-pannonicum-i/Details'
            }

    for key in plants:
        html = plants[key]
        path = key
        scrape_to_file(html, path)


if __name__ == '__main__':
    main()
