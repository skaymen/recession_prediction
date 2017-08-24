import config as c

from bs4 import BeautifulSoup
import requests

date = c.FFR_DATE
url = c.FFR_URL

def get_effr():
    # Get HTML from site.
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = []

    for table in soup.find_all('table'):
        if table.get("id") == "TBLDetails":
            for row in table:
                for x in row:
                    data.append(x)

    for index, elem in enumerate(data):
        if date in str(elem):
            for x in data[index + 2]:
                effr = float(str(x).strip())
                break

    return effr



get_effr()