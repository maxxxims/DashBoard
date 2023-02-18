from urllib.request import urlopen
import json
import numpy as np
import pandas as pd
import plotly.express as px


def amount_by_county_map_p2(data,column):
  arr = []
  df_n = pd.DataFrame()
  df_n['Округ'] = data["Округ"].unique()
  for district in data['Округ'].unique():
    arr.append(np.sum(np.array(data.loc[data['Округ'] == district , column])))
  df_n[f'Суммарный показатель'] = np.array(arr)
  return df_n

def amount_by_region_map_p2(data,column):
  arr =[]
  df_n = pd.DataFrame()
  df_n['Регион'] = data['Регион'].unique()
  for district in data['Регион'].unique():
    arr.append(np.array(data.loc[data['Регион'] == district , column])[0])
  df_n[f'Суммарный показатель'] = np.array(arr)
  return df_n


def building_map_by_region_p2(df_map, counties):
  df_1 = pd.DataFrame()
  df_1['name'] = [counties['features'][i]['properties']['name'] for i in range(len(counties['features']))]
  true_arr = np.array(df_1['name'])
  rep = []
  for i in np.array(df_map['Регион']):
    if i not in np.array(df_1['name']):
      rep.append(i)
  df_map['Регион']=df_map['Регион'].replace(rep, ['Астраханская область','Кабардино-Балкарская республика',
                               'Карачаево-Черкесская республика',
                                   'Адыгея','Алтай','Башкортостан','Бурятия','Дагестан','Ингушетия',
                                   'Республика Крым','Марий Эл','Северная Осетия - Алания','Татарстан',
                                   'Тыва','Севастополь','Удмуртская республика','Чеченская республика','Чувашия'])
  df_map = df_map[df_map['Регион'].isin(true_arr)]
  fig = px.choropleth_mapbox(df_map, geojson=counties, locations='Регион',
                           color = 'Суммарный показатель',
                           featureidkey = 'properties.name',
                           color_continuous_scale="Viridis",
                           mapbox_style="carto-positron",
                           zoom=2, center = {"lat": 71, "lon": 105},
                           opacity=0.5,
                           #labels={'unemp':'unemployment rate'}
                          )
  fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
  return fig