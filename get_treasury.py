import requests
from lxml import html
from bs4 import BeautifulSoup

url = "https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yieldYear&year=2017"

def get_yields(url):
    # Get HTML from site.
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find_all('table')
    for t in table:
        print(t)
        class_name = t.get("class")
        if (class_name == "t-chart"):
            print(t)



get_yields(url)
