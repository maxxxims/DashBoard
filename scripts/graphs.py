import plotly.express as px
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


COLOR1 = ['#A99FE0', '#897AD6', '#b3e427', '#8eaf0c']

def drawing_graphs(column_name,df):
    if df[column_name].dtypes == "object":
        d = df[column_name].value_counts(normalize=False).rename_axis(column_name).reset_index(name='fraction')
        fig = px.pie(d, values='fraction', names=f'{column_name}', title=f'{column_name}',color_discrete_sequence=px.colors.sequential.Rainbow)
    elif df[column_name].dtypes in ["int64", "float64"]:
        d = df[column_name] 
        fig = px.histogram(d, x=f'{column_name}')
    return fig



def amount_by_county_p2(data,column,county,all):
  p2 = ['Региональные органы исполнительной власти',
               'Бюджетные учреждения',
               'Муниципальные органы испольнительной власти',
               'Муниципальные бюджетные учреждения']
  df_n = pd.DataFrame()
  if all:
    county = data['Округ'].unique()
    df_n['Наименование'] = np.array(p2)
    arr = []
    for i in p2:
      arr.append(np.array(np.sum(np.array(data.loc[data['Округ'].isin(county), f'{i} ({column})']))))
    df_n[f'Сумма по {column}'] =  np.array(arr)
    fig = px.pie(df_n, values=f'Сумма по {column}', names='Наименование',
                 title=f'Распределение {column} по облостям',color_discrete_sequence=COLOR1)
    return fig
  else:
    df_n['Наименование'] = np.array(p2)
    arr = []
    for i in p2:
      arr.append(np.array(np.sum(np.array(data.loc[data['Округ'].isin(county), f'{i} ({column})']))))
    df_n[f'Сумма по {column}'] =  np.array(arr)
    t = f'Распределение {column} в '+ ', '.join(county)
    fig = px.pie(df_n, values=f'Сумма по {column}', names='Наименование',
                 title=t, color_discrete_sequence=COLOR1)
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
    print(df_n)
    for i in p2:
      arr.append(np.array(np.sum(np.array(data.loc[data['Округ'].isin(county), f'{i} ({column})']))))
    df_n[f'Сумма по {column}'] =  np.array(arr)
    fig = px.pie(df_n, values=f'Сумма по {column}', names='Наименование', 
                title=f'Распределение {column} по облостям',color_discrete_sequence=COLOR1)
    return fig
  else:
    df_n['Наименование'] = np.array(p2)
    arr = []
    for i in p2:
      arr.append(np.array(np.sum(np.array(data.loc[data['Регион'].isin(county), f'{i} ({column})']))))
    df_n[f'Сумма по {column}'] =  np.array(arr)
    t = f'Распределение {column} в '+ ', '.join(county)
    fig = px.pie(df_n, values=f'Сумма по {column}',
                 names='Наименование',
                 title=t,
                 color_discrete_sequence=COLOR1)
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
    fig = px.pie(df_n, values=f'Сумма по {column}', names='Наименование', title=f'Распределение {column} по облостям',color_discrete_sequence=COLOR1)
    return fig
  else:
    df_n['Наименование'] = np.array(p4)
    arr = []
    for i in p4:
      arr.append(np.array(np.sum(np.array(data.loc[data['Округ'].isin(county), f'{i} ({column})']))))
    df_n[f'Сумма по {column}'] =  np.array(arr)
    df_n['Наименование'] = np.array(p4_short)
    t = f'Распределение {column} в '+ ', '.join(county)
    fig = px.pie(df_n, values=f'Сумма по {column}', names='Наименование',
                 title=t,
                 color_discrete_sequence=COLOR1)
    return fig


def region_comparison_2(data,param,region_1,region_2):
  p2 = ['Региональные органы исполнительной власти',
        'Бюджетные учреждения','Муниципальные органы испольнительной власти',
        'Муниципальные бюджетные учреждения']
  ################################      
  df_n_1 = pd.DataFrame()
  df_n_1['Наименование'] = np.array(p2)
  arr = []
  for i in p2:
    arr.append(np.array(np.array(data.loc[data['Регион'] == region_1, f'{i} ({param})'])[0]))
  df_n_1[f'Сумма по {param}'] =  np.array(arr)
  ################################
  df_n_2 = pd.DataFrame()
  df_n_2['Наименование'] = np.array(p2)
  arr = []
  for i in p2:
    arr.append(np.array(np.array(data.loc[data['Регион'] == region_2, f'{i} ({param})'])[0]))
  df_n_2[f'Сумма по {param}'] =  np.array(arr)
  ################################
  fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
  fig.add_trace(go.Pie(labels=df_n_1['Наименование'], values=df_n_1[f'Сумма по {param}'], name=f"{region_1}", marker=dict(colors=list(reversed(COLOR1)))),
                1, 1)
  fig.add_trace(go.Pie(labels=df_n_2['Наименование'], values=df_n_2[f'Сумма по {param}'], name=f"{region_2}", marker=dict(colors=list(reversed(COLOR1)))),
                1, 2)
  fig.update_traces(hole=.4, hoverinfo="label+percent+name")

  fig.update_layout(
      title_text=f"Сравнение {region_1} и {region_2} по {param}",
      annotations=[dict(text=f'{region_1}', x=0, y=1.1, font_size=15, showarrow=False),
                   dict(text=f'{region_2}', x=1, y=1.1, font_size=15, showarrow=False)])
  
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
    fig = px.pie(df_n, values=f'Сумма по {column}', names='Наименование', title=f'Распределение {column} по облостям',color_discrete_sequence=COLOR1)
    return fig
  else:
    df_n['Наименование'] = np.array(p4)
    arr = []
    for i in p4:
      arr.append(np.array(np.sum(np.array(data.loc[data['Регион'].isin(county), f'{i} ({column})']))))
    df_n[f'Сумма по {column}'] =  np.array(arr)
    df_n['Наименование'] = np.array(p4_short)
    t = f'Распределение {column} в '+ ', '.join(county)
    fig = px.pie(df_n, values=f'Сумма по {column}', names='Наименование',
                 title=t,
                 color_discrete_sequence=COLOR1)
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
  df_n_1 = pd.DataFrame()
  df_n_1['Наименование'] = np.array(p4)
  arr = []
  for i in p4:
    arr.append(np.array(np.array(data.loc[data['Регион'] == region_1, f'{i} ({param})'])[0]))
  df_n_1[f'Сумма по {param}'] =  np.array(arr)
  df_n_1['Наименование'] = np.array(p4_short)

  df_n_2 = pd.DataFrame()
  df_n_2['Наименование'] = np.array(p4)
  arr = []
  for i in p4:
    arr.append(np.array(np.array(data.loc[data['Регион'] == region_2, f'{i} ({param})'])[0]))
  df_n_2[f'Сумма по {param}'] =  np.array(arr)
  df_n_2['Наименование'] = np.array(p4_short)

  fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
  fig.add_trace(go.Pie(labels=df_n_1['Наименование'], values=df_n_1[f'Сумма по {param}'], name=f"{region_1}",marker=dict(colors=list(reversed(COLOR1)))),
                1, 1)
  fig.add_trace(go.Pie(labels=df_n_2['Наименование'], values=df_n_2[f'Сумма по {param}'], name=f"{region_2}", marker=dict(colors=list(reversed(COLOR1)))),
                1, 2)
  fig.update_traces(hole=.4, hoverinfo="label+percent+name")
  fig.update_layout(
      title_text=f"Сравнение {region_1} и {region_2} по {param}",
      annotations=[dict(text=f'{region_1}', x=0, y=0.01, font_size=15, showarrow=False),
                   dict(text=f'{region_2}', x=1, y=0.01, font_size=15, showarrow=False)])
  
  return fig


def statistics_by_year(data, chapter):
  names = [2016, 2017, 2018, 2019, 2020, 2021]
  arr = np.array(data.loc[data['Раздел'] == chapter, names])[0]
  fig = px.line(x=names, y=arr,title=f"{chapter}")
  return fig





def draw_horizontal_graph(data):
    summ = {
            'СФО': 0,
            'ДФО': 0,
            'СЗФО': 0,
            'ПФО': 0,
            'ЮФО': 0,
            'УФО': 0,
            'ЦФО': 0,
            'СКФО': 0
        }
    df = pd.DataFrame()
    df['Расходы'] = data[['Региональные органы исполнительной власти (Всего объeм финансирования, руб)',
                           'Бюджетные учреждения (Всего объeм финансирования, руб)',
                           'Муниципальные органы испольнительной власти (Всего объeм финансирования, руб)',
                           'Муниципальные бюджетные учреждения (Всего объeм финансирования, руб)',
                           ]].sum(
        axis=1)

    df['Округ'] = data['Округ']

    for index, row in df.iterrows():
        summ[row['Округ']] += row['Расходы']

    fig = go.Figure(go.Bar(
        x=['СФО', 'ДФО', 'СЗФО', 'ПФО', 'ЮФО', 'УФО', 'ЦФО', 'СКФО'],
        y=[v for k, v in summ.items()], name="Расходы всех структур по регионам"))
    fig.layout.colorway = ['#897AD6']
    fig.update_layout(
        xaxis_title='Округ',  # title for x axis
        yaxis_title='Траты в руб.',
        plot_bgcolor='white',)

    return fig


def statistics_by_year(data, chapter):
  names = [2016, 2017, 2018, 2019, 2020, 2021]
  arr = np.array(data.loc[data['Раздел'] == chapter, names])[0]
  
  fig = px.line(x=names, y=arr,title=f"{chapter}")
  return fig