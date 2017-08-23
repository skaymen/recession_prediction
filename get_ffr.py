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
                # for index, elem in enumerate(row):
                #     if date in str(elem):
                #         print(row[index + 1])

    for index, elem in enumerate(data):
        if date in str(elem):
            print(data)
            print(str(data[index + 1]))
    #     print("x" + str(i).replace(" ", ""))
    #     if date in str(elem):
    #         for x in elem:
    #             print(x)
            # print(elem)
            # print(str(data[index + 1]) + "x")

                    # data.append(str(i).replace(" ", ""))


    # for td in soup.find_all('td'):
    #     # print td.get("class")
    #     if (td.get("class") == ["dirColTight", "numData"]):
    #         for item in td:
    #             for i in item:
    #                 data.append(i)
    #
    # print(data)


get_effr()