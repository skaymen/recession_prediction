from bs4 import BeautifulSoup
import requests


def get_yields(date, url_prefix):

    year = "20" + date[6:]
    url = url_prefix + year

    # Get HTML from site.
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = []

    # Find the table of data and put it into an array
    for row in soup.find_all('tr'):
        if (row.get("class") == ["oddrow"] or row.get("class") == ["evenrow"]):
            for item in row:
                for i in item:
                    data.append(i)

    # Return the two yield figures as a dictionary
    yields = {}

    for index, elem in enumerate(data):
        if (elem == date):
            yields['3_month'] = float(data[index + 2])
            yields['10_year'] = float(data[index + 9])

    return yields


