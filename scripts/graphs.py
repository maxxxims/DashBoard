import plotly.express as px
import numpy as np
import pandas as pd




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
    fig = px.pie(df_n, values=f'Сумма по {column}', names='Наименование', title=f'Распределение {column} по облостям',color_discrete_sequence=px.colors.sequential.RdBu)
    return fig
  else:
    df_n['Наименование'] = np.array(p2)
    arr = []
    for i in p2:
      arr.append(np.array(np.sum(np.array(data.loc[data['Округ'] == county, f'{i} ({column})']))))
    df_n[f'Сумма по {column}'] =  np.array(arr)
    fig = px.pie(df_n, values=f'Сумма по {column}', names='Наименование', title=f'Распределение {column} в {county}',color_discrete_sequence=px.colors.sequential.RdBu)
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