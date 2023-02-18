
import numpy as np
import pandas as pd
from dash import dcc


def getSelectorsForTab1(df, pageNumber):
    table = {}
    for col in df.columns:
        if len(df[col].unique()) <= 10:
            temp = []
            for k in df[col].unique():
                temp.append({'label': k, 'value': k})
            table[col] = temp
    

    
    options = [{'label': 'Customer_Age', 'value': 'Customer_Age'}, 
            {'label': 'Gender', 'value': 'Gender'},
            {'label': 'Card_Category', 'value': 'Card_Category'}]


    card_selector = dcc.Dropdown(
        id='card_selector_' + pageNumber,
        options=options,
        value='Customer_Age',
        multi=False
    )


    option_special = []

    for key in table.keys():
        option_special.append({'label': key, 'value': key})

    option_category = dcc.Dropdown(
                        id='table_columns_' + pageNumber,
                        options=option_special,
                        value='',
                        multi=False
                                )



    selector = dcc.Dropdown(
                        id='table_values_' + pageNumber,
                        options=[],
                        value='',
                        multi=False
                                )




    age_selector = dcc.RangeSlider(
        id="range-slider",
        min=min(df["Customer_Age"]),
        max=max(df["Customer_Age"]),
        marks={25: '25', 30: '30', 35: '35', 40: '40', 45: '45', 50: '50', 55: '55', 60: '60', 65: '65', 70: '70'},
        step=1,
        value=[26, 73]
    )

    return card_selector, option_category, selector, age_selector



def getSelectorsForTab2(df, pageNumber):
    table = ['Кол-во структур, ед',
            'Всего кол-во сотрудников, чел',
            'Всего с профильным образованием',
            'Всего объeм финансирования, руб',
            'Расходы на мероприятия',
            'Расходы на адм функции',
            'Расходы на ремонт']

    county_options = df['Округ'].unique()
    county_options = np.append('Все округи', county_options)

    region_options = df['Регион'].unique()
    region_options = np.append('Все регионы', region_options)

    special_options = []

    for key in table:
        special_options.append({'label': key, 'value': key})

    category_selector = dcc.Dropdown(
                        id='category-selector-' + pageNumber,
                        options=special_options,
                        value=table[0],
                        multi=False
                                )

    table2 = ['Муниципальные бюджетные учреждения',
                    'Муниципальные органы испольнительной власти',
                    'Бюджетные учреждения',
                    'Региональные органы исполнительной власти']

    type_options = []
    for key in table2:
        type_options.append({'label': key, 'value': key})

    type_selector = dcc.Dropdown(
                        id='type-selector-' + pageNumber,
                        options=type_options,
                        value=table2[0],
                        multi=False
                                )


    county_selector = dcc.Dropdown(
                        id='county-selector-' + pageNumber,
                        options=county_options,
                        value='Все округи',
                        multi=False
                                )


    region_selector = dcc.Dropdown(
                        id='region-selector-' + pageNumber,
                        options=region_options,
                        value='',
                        multi=False
                                )
    





    return category_selector, county_selector, region_selector, type_selector



def getSelectorsForTab4(df, pageNumber):
    table = ['Кол-во рег. объединений, ед', 'Кол-во мест. объединений, ед','Число членов рег. объединений, чел',
            'Число членов мест. объединений, чел','Число уч-в мер-й рег. объединений, чел',
            'Число уч-в мер-й мест. объединений, чел','Объeм фин.поддержки рег. объединений, руб',
            'Объeм фин.поддержки мест. объединений, руб']

    county_options = df['Округ'].unique()
    county_options = np.append('Все округи', county_options)

    region_options = df['Регион'].unique()
    region_options = np.append('Все регионы', region_options)

    special_options = []

    for key in table:
        special_options.append({'label': key, 'value': key})

    category_selector = dcc.Dropdown(
                        id='category-selector-' + pageNumber,
                        options=special_options,
                        value=table[0],
                        multi=False
                                )

    table2 = ['Общественные объединения, включенные в реестр детских и молодeжных объединений, пользующихся государственной поддержкой',
            'Объединения, включенные в перечень партнеров органа исполнительной власти, реализующего государственную молодeжную политику',
            'Политические молодeжные общественные объединения',
            'Молодeжные патрули / добровольные молодeжные дружины']

    type_options = []
    for key in table2:
        type_options.append({'label': key, 'value': key})

    type_selector = dcc.Dropdown(
                        id='type-selector-' + pageNumber,
                        options=type_options,
                        value=table2[0],
                        multi=False
                                )


    county_selector = dcc.Dropdown(
                        id='county-selector-' + pageNumber,
                        options=county_options,
                        value='Все округи',
                        multi=False
                                )


    region_selector = dcc.Dropdown(
                        id='region-selector-' + pageNumber,
                        options=region_options,
                        value='',
                        multi=False
                                )
    

    region_selector_vs1 = dcc.Dropdown(
                        id='region-selector-vs1-' + pageNumber,
                        options=region_options[1:],
                        value='',
                        multi=False
                                )

    region_selector_vs2 = dcc.Dropdown(
                        id='region-selector-vs2-' + pageNumber,
                        options=region_options[1:],
                        value='',
                        multi=False
                                )





    return category_selector, county_selector, region_selector, type_selector, region_selector_vs1, region_selector_vs2
