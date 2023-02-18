import plotly.express as px
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def drawing_graphs(column_name,df):
    if df[column_name].dtypes == "object":
        d = df[column_name].value_counts(normalize=False).rename_axis(column_name).reset_index(name='fraction')
        fig = px.pie(d, values='fraction', names=f'{column_name}', title=f'{column_name}',color_discrete_sequence=px.colors.sequential.RdBu)
    elif df[column_name].dtypes in ["int64", "float64"]:
        d = df[column_name] 
        fig = px.histogram(d, x=f'{column_name}')
    return fig



def amount_by_county_p2(data,column,county,all):
  p2 = ['Региональные органы исполнительной власти',
        'Бюджетные учреждения','Муниципальные органы испольнительной власти',
        'Муниципальные бюджетные учреждения']
  df_n = pd.DataFrame()
  if all:
    county = data['Округ'].unique()
    df_n['Наименование'] = np.array(p2)
    arr = []
    for i in p2:
      arr.append(np.array(np.sum(np.array(data.loc[data['Округ'].isin(county), f'{i} ({column})']))))
    df_n[f'Сумма по {column}'] =  np.array(arr)
    fig = px.pie(df_n, values=f'Сумма по {column}', names='Наименование', title=f'Распределение {column} по облостям',color_discrete_sequence=px.colors.sequential.Rainbow)
    return fig
  else:
    df_n['Наименование'] = np.array(p2)
    arr = []
    for i in p2:
      arr.append(np.array(np.sum(np.array(data.loc[data['Округ'] == county, f'{i} ({column})']))))
    df_n[f'Сумма по {column}'] =  np.array(arr)
    fig = px.pie(df_n, values=f'Сумма по {column}', names='Наименование', title=f'Распределение {column} в {county}',color_discrete_sequence=px.colors.sequential.Rainbow)
    return fig


def amount_by_region_p2(data,column,county,all):
  p2 = ['Региональные органы исполнительной власти',
        'Бюджетные учреждения','Муниципальные органы испольнительной власти',
        'Муниципальные бюджетные учреждения']
  df_n = pd.DataFrame()
  if all:
    county = data['Округ'].unique()
    df_n['Наименование'] = np.array(p2)
    arr = []
    for i in p2:
      arr.append(np.array(np.sum(np.array(data.loc[data['Округ'].isin(county), f'{i} ({column})']))))
    df_n[f'Сумма по {column}'] =  np.array(arr)
    fig = px.pie(df_n, values=f'Сумма по {column}', names='Наименование', title=f'Распределение {column} по облостям',color_discrete_sequence=px.colors.sequential.RdBu)
    return fig
  else:
    df_n['Наименование'] = np.array(p2)
    arr = []
    for i in p2:
      arr.append(np.array(np.array(data.loc[data['Регион'] == county, f'{i} ({column})'])[0]))
    df_n[f'Сумма по {column}'] =  np.array(arr)
    fig = px.pie(df_n, values=f'Сумма по {column}', names='Наименование', title=f'Распределение {column} в {county}',color_discrete_sequence=px.colors.sequential.RdBu)
    return fig



def amount_by_county_p4(data,column,county,all):
  p4 = ['Общественные объединения, включенные в реестр детских и молодeжных объединений, пользующихся государственной поддержкой',
        'Объединения, включенные в перечень партнеров органа исполнительной власти, реализующего государственную молодeжную политику',
        'Политические молодeжные общественные объединения',
        'Молодeжные патрули / добровольные молодeжные дружины']
  p4_short = ['Общественные объединения, включенные в реестр',
              'Объединения, включенные в перечень партнеров',
              'Политические молодeжные общественные объединения',
        'Молодeжные патрули / добровольные молодeжные дружины']
  df_n = pd.DataFrame()
  if all:
    county = data['Округ'].unique()
    df_n['Наименование'] = np.array(p4)
    arr = []
    for i in p4:
      arr.append(np.array(np.sum(np.array(data.loc[data['Округ'].isin(county), f'{i} ({column})']))))
    df_n[f'Сумма по {column}'] =  np.array(arr)
    df_n['Наименование'] = np.array(p4_short)
    fig = px.pie(df_n, values=f'Сумма по {column}', names='Наименование', title=f'Распределение {column} по облостям',color_discrete_sequence=px.colors.sequential.PuBu)
    return fig
  else:
    df_n['Наименование'] = np.array(p4)
    arr = []
    for i in p4:
      arr.append(np.array(np.sum(np.array(data.loc[data['Округ'] == county, f'{i} ({column})']))))
    df_n[f'Сумма по {column}'] =  np.array(arr)
    df_n['Наименование'] = np.array(p4_short)
    fig = px.pie(df_n, values=f'Сумма по {column}', names='Наименование',
                 title=f'Распределение {column} в {county}',
                 color_discrete_sequence=px.colors.sequential.RdBu)
    return fig


def amount_by_region_p4(data,column,county,all):
  p4 = ['Общественные объединения, включенные в реестр детских и молодeжных объединений, пользующихся государственной поддержкой',
        'Объединения, включенные в перечень партнеров органа исполнительной власти, реализующего государственную молодeжную политику',
        'Политические молодeжные общественные объединения',
        'Молодeжные патрули / добровольные молодeжные дружины']
  p4_short = ['Общественные объединения, включенные в реестр',
              'Объединения, включенные в перечень партнеров',
              'Политические молодeжные общественные объединения',
        'Молодeжные патрули / добровольные молодeжные дружины']
  df_n = pd.DataFrame()
  if all:
    county = data['Округ'].unique()
    df_n['Наименование'] = np.array(p4)
    arr = []
    for i in p4:
      arr.append(np.array(np.sum(np.array(data.loc[data['Округ'].isin(county), f'{i} ({column})']))))
    df_n[f'Сумма по {column}'] =  np.array(arr)
    df_n['Наименование'] = np.array(p4_short)
    fig = px.pie(df_n, values=f'Сумма по {column}', names='Наименование', title=f'Распределение {column} по облостям',color_discrete_sequence=px.colors.sequential.Rainbow)
    return fig
  else:
    df_n['Наименование'] = np.array(p4)
    arr = []
    for i in p4:
      arr.append(np.array(np.array(data.loc[data['Регион'] == county, f'{i} ({column})'])[0]))
    df_n[f'Сумма по {column}'] =  np.array(arr)
    df_n['Наименование'] = np.array(p4_short)
    fig = px.pie(df_n, values=f'Сумма по {column}', names='Наименование', title=f'Распределение {column} в {county}',color_discrete_sequence=px.colors.sequential.Rainbow)
    return fig



def region_comparison(data,param,region_1,region_2):
  p4 = ['Общественные объединения, включенные в реестр детских и молодeжных объединений, пользующихся государственной поддержкой',
        'Объединения, включенные в перечень партнеров органа исполнительной власти, реализующего государственную молодeжную политику',
        'Политические молодeжные общественные объединения',
        'Молодeжные патрули / добровольные молодeжные дружины']
  p4_short = ['Общественные объединения, включенные в реестр',
              'Объединения, включенные в перечень партнеров',
              'Политические молодeжные общественные объединения',
        'Молодeжные патрули / добровольные молодeжные дружины']
  ################################      
  df_n_1 = pd.DataFrame()
  df_n_1['Наименование'] = np.array(p4)
  arr = []
  for i in p4:
    arr.append(np.array(np.array(data.loc[data['Регион'] == region_1, f'{i} ({param})'])[0]))
  df_n_1[f'Сумма по {param}'] =  np.array(arr)
  df_n_1['Наименование'] = np.array(p4_short)
  ################################
  df_n_2 = pd.DataFrame()
  df_n_2['Наименование'] = np.array(p4)
  arr = []
  for i in p4:
    arr.append(np.array(np.array(data.loc[data['Регион'] == region_2, f'{i} ({param})'])[0]))
  df_n_2[f'Сумма по {param}'] =  np.array(arr)
  df_n_2['Наименование'] = np.array(p4_short)
  ################################
  fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
  fig.add_trace(go.Pie(labels=df_n_1['Наименование'], values=df_n_1[f'Сумма по {param}'], name=f"{region_1}"),
                1, 1)
  fig.add_trace(go.Pie(labels=df_n_2['Наименование'], values=df_n_2[f'Сумма по {param}'], name=f"{region_2}"),
                1, 2)
  fig.update_traces(hole=.4, hoverinfo="label+percent+name")

  fig.update_layout(
      title_text=f"Сравнение {region_1} и {region_2} по {param}",
      annotations=[dict(text=f'{region_1}', x=0, y=1, font_size=15, showarrow=False),
                   dict(text=f'{region_2}', x=1, y=1, font_size=15, showarrow=False)])
  
  return fig