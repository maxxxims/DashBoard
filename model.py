import numpy as np
import pandas as pd
from dash import dcc
from urllib.request import urlopen
import json


path = "data/Форма М1 2021.xlsx"
#sheet_name = 'Р2'


def update_P2(path,sheet_name):
  df = pd.read_excel(path,sheet_name = sheet_name)
  Names = df["Наименование"].unique()
#   for i in range(len(Names)):
#     Names[i] = Names[i].replace('\n','')

  columns = np.array(df.columns)[5:]
  df_n = pd.DataFrame()
  df_n['Регион'] = df["Регион"].unique()
  for k in Names:
    for c in columns:
      df_n[f'{k} ({c})'] = np.array(df.loc[df['Наименование'] == f'{k}', f'{c}'])
  df_n = df_n.fillna(0)
  frame = pd.read_csv('data/d.csv', sep="\t")
  buff = [el for el in frame["Округ"]]
  sort = df_n.sort_values(['Регион'], axis=0)
  sort["Округ"] = buff

  return sort


class DATA:
    data = []
    number = 0

    def __init__(self, file_number) -> None:
        self.number = file_number


    def setDataSet(self):

        self.data = update_P2(path, sheet_name=f'Р{str(self.number)}')

        if self.number == 2:
            self.data = pd.read_csv("data/Р2.csv")


    def getDataSet(self):
        return self.data


df2 = DATA(file_number=2)
df2.setDataSet()

url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson"
counties = ''
with urlopen(url) as response:
    counties = json.load(response)

#print(df2['Регион'].unique())

# from scripts.graphs import amount_by_county_p2

# fig = amount_by_county_p2(df2, 'Всего кол-во сотрудников, чел', 'ЦФО', all=False)

# fig.show()