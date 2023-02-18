
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

    option_special = []

    for key in table:
        option_special.append({'label': key, 'value': key})

    category_selector = dcc.Dropdown(
                        id='category-selector-' + pageNumber,
                        options=option_special,
                        value=table[0],
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






    return category_selector, county_selector, region_selector
