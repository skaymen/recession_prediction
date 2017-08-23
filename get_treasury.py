import config as c

from bs4 import BeautifulSoup
import requests

date = c.TREASURY_DATE
url_prefix = c.TREASURY_URL_PREFIX
year = "20" + date[6:]
url = url_prefix + year



def get_yields():
    # Get HTML from site.
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = []

    for row in soup.find_all('tr'):
        if (row.get("class") == ["oddrow"] or row.get("class") == ["evenrow"]):
            for item in row:
                for i in item:
                    data.append(i)

    for index, elem in enumerate(data):
        if (elem == date):
            three_month = data[index + 2]
            ten_year = data[index + 9]

    print(three_month)
    print(ten_year)





get_yields()
