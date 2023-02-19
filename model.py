import numpy as np
import pandas as pd
from dash import dcc
from urllib.request import urlopen
import json


path = "data/Форма М1 2021.xlsx"


def update_P1(path,sheet_name):
  df = pd.read_excel(path,sheet_name = sheet_name)
  df = df.drop(columns=['№ строки', 'Год'])
  df = df.fillna(0)
  columns = np.array(df.columns[3:-2])
  df_n = pd.DataFrame()
  df_n['Регион'] = df["Регион"].unique()
  for c in columns:
    arr = []
    for k in np.array(df["Регион"].unique()):
      arr.append(np.sum(np.array(df.loc[df["Регион"] == k, c])))
    df_n[c] = arr
  df_n = df_n.fillna(0)
  ###ДОбавление Округа(костыль)
  frame = pd.read_csv('data/d.csv', sep="\t")
  buff = [el for el in frame["Округ"]]
  sort = df_n.sort_values(['Регион'], axis=0)
  sort["Округ"] = buff
  return sort


def update_P2(path,sheet_name):
  df = pd.read_excel(path,sheet_name = sheet_name)
  Names = ['      региональный орган\n      исполнительной власти',
           '      бюджетные\n      учреждения',
           '      муниципальные\n      органы\n      испольнительной власти',
           '      муниципальные\n      бюджетные\n      учреждения']

  new_Names = ['Региональные органы исполнительной власти',
               'Бюджетные учреждения',
               'Муниципальные органы испольнительной власти',
               'Муниципальные бюджетные учреждения']
  columns = np.array(df.columns)[5:]
  df_n = pd.DataFrame()
  df_n['Регион'] = df["Регион"].unique()
  for k in range(len(Names)):
    for c in columns:
      df_n[f'{new_Names[k]} ({c})'] = np.array(df.loc[df['Наименование'] == f'{Names[k]}', f'{c}'])
  df_n = df_n.fillna(0)
  frame = pd.read_csv('data/d.csv', sep="\t")
  buff = [el for el in frame["Округ"]]
  sort = df_n.sort_values(['Регион'], axis=0)
  sort["Округ"] = buff
  return sort


def update_P8(path, sheet_name):
  sheet_name = 'статистика по годам'
  df = pd.read_excel(path,sheet_name = sheet_name)
  new_names = [
    'Объем финансирования молодежной политики из бюджета СРФ',
    'Объем финансирования молодежной политики из бюджета ОМСУ',
    'Количество грантов, выданных физическим и юридическим лица',
    'Объем грантовых средств, выданных физическим и юридическим лицам',
    'Количество POO, пользующихся государственной поддержкой',
    'Количество местных общественных объединений, пользующихся поддержкой',
    'Количество органов молодежного самоуправления',
    'Количество молодежных форумов, прошедших на территории СРФ',
    'Численность участников молодежных форумов',
    'Объем финансирования молодежных форумов из средств бюджетов СРФ',
    'Объем финансирования молодежных форумов из средств ОМСУ']
  df['Раздел'] = new_names
  return df
  

def update_P4(path,sheet_name):
  df = pd.read_excel(path,sheet_name = sheet_name)
  Names = ['Общественные объединения, включенные в реестр детских и молодeжных объединений, пользующихся государственной поддержкой',
           'Объединения, включенные в перечень партнеров органа исполнительной власти, реализующего государственную молодeжную политику / работающего с молодeжью (исключая ситуации, включенные в реестр согласно Федеральному закону № 98-ФЗ)',
           'Политические молодeжные общественные объединения',
           'Молодeжные патрули / добровольные молодeжные дружины']

  new_Names = ['Общественные объединения, включенные в реестр детских и молодeжных объединений, пользующихся государственной поддержкой',
        'Объединения, включенные в перечень партнеров органа исполнительной власти, реализующего государственную молодeжную политику',
        'Политические молодeжные общественные объединения',
        'Молодeжные патрули / добровольные молодeжные дружины']
  columns = np.array(df.columns)[5:-3]
  df_n = pd.DataFrame()
  df_n['Регион'] = df["Регион"].unique()
  for k in range(len(Names)):
    for c in columns:
      df_n[f'{new_Names[k]} ({c})'] = np.array(df.loc[df['Наименование'] == f'{Names[k]}', f'{c}'])
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
      if self.number == 1:
        self.data = update_P1(path, sheet_name=f'Р{str(self.number)}')

      if self.number == 2:
        self.data = update_P2(path, sheet_name=f'Р{str(self.number)}')

      if self.number == 4:
        self.data = update_P4(path, sheet_name=f'Р{str(self.number)}')

      if self.number == 8:
        self.data = update_P8(path, sheet_name=f'Р{str(self.number)}')


    def getDataSet(self):
        return self.data


df2 = DATA(file_number=2)
df2.setDataSet()


df4 = DATA(file_number=4)
df4.setDataSet()

df1 = DATA(file_number=1)
df1.setDataSet()

df8 = DATA(file_number=8)
df8.setDataSet()



url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson"
counties = ''
with urlopen(url) as response:
    counties = json.load(response)
