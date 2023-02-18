import numpy as np
import pandas as pd

from dash import dcc

from urllib.request import urlopen
import json

df2 = pd.read_csv("data/Р2.csv")

url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson"
counties = ''
with urlopen(url) as response:
    counties = json.load(response)

#print(df2['Регион'].unique())

# from scripts.graphs import amount_by_county_p2

# fig = amount_by_county_p2(df2, 'Всего кол-во сотрудников, чел', 'ЦФО', all=False)

# fig.show()