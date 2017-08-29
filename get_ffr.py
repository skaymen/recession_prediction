import config as c

from bs4 import BeautifulSoup
import requests


def get_effr(date, url):

    # Get HTML from site.
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = []

    # Grab all data inside the table
    for table in soup.find_all('table'):
        if table.get("id") == "TBLDetails":
            for row in table:
                for x in row:
                    data.append(x)

    effr = -1
    # Find the ffr using the date given
    for index, elem in enumerate(data):
        if date in str(elem):
            for x in data[index + 2]:
                effr = float(str(x).strip())
                break

    return effr
