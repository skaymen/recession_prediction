import requests
from lxml import html
from bs4 import BeautifulSoup

url = "https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yieldYear&year=2017"

def get_yields(url):
    # Get HTML from site.
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for row in soup.find_all('tr'):
        if (row.get("class") == ["oddrow"] or row.get("class") == ["evenrow"]):
            for item in row:
                for i in item:
                    print(i)



get_yields(url)
