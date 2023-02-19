
import numpy as np
import pandas as pd
from dash import dcc



def getTables(pageNumber):
    table, table2 = [], []

    if int(pageNumber) ==1:
        table = ['Бюджет СРФ, руб', 'Бюджет МО, руб', 'Кол-во грантов',
                'Бюджет грантов, руб',
                'Численность молодeжи, задействованной в программных мероприятиях по направлению',
                'Количество детских и молодeжных общественных объединений, работающих по данному ']


    if int(pageNumber) == 2:
        table = ['Кол-во структур, ед',
            'Всего кол-во сотрудников, чел',
            'Всего с профильным образованием',
            'Всего объeм финансирования, руб',
            'Расходы на мероприятия',
            'Расходы на адм функции',
            'Расходы на ремонт']
        
        table2 = ['Муниципальные бюджетные учреждения',
                    'Муниципальные органы испольнительной власти',
                    'Бюджетные учреждения',
                    'Региональные органы исполнительной власти']

    elif int(pageNumber) == 4:
        table = ['Кол-во рег. объединений, ед', 'Кол-во мест. объединений, ед','Число членов рег. объединений, чел',
            'Число членов мест. объединений, чел','Число уч-в мер-й рег. объединений, чел',
            'Число уч-в мер-й мест. объединений, чел','Объeм фин.поддержки рег. объединений, руб',
            'Объeм фин.поддержки мест. объединений, руб']

        table2 = ['Общественные объединения, включенные в реестр детских и молодeжных объединений, пользующихся государственной поддержкой',
                'Объединения, включенные в перечень партнеров органа исполнительной власти, реализующего государственную молодeжную политику',
                'Политические молодeжные общественные объединения',
                'Молодeжные патрули / добровольные молодeжные дружины']
        

    elif int(pageNumber) == 8:
        table = [
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

    return table, table2



def getSelectorsForTab(df, pageNumber):
    table, table2 = getTables(pageNumber)
    county_options = []
    for el in np.append('Все округи', df['Округ'].unique()):
        county_options.append({'label': el, 'value': el})



    region_options = []
    for el in np.append('Все регионы', df['Регион'].unique()):
        region_options.append({'label': el, 'value': el})


    special_options = []

    for key in table:
        special_options.append({'label': key, 'value': key})

    category_selector = dcc.Dropdown(
                        id='category-selector-' + pageNumber,
                        options=special_options,
                        value=table[0],
                        multi=False
                                )

    

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
                        value=['Все округи'],
                        multi=True
                                )


    region_selector = dcc.Dropdown(
                        id='region-selector-' + pageNumber,
                        options=region_options,
                        value=[''],
                        multi=True
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



def getSelectorsForTab1(df, pageNumber):
    
    table, _ = getTables(pageNumber)

    options = []

    for el in table:
        options.append({'label': el, 'value': el})

    category_selector = dcc.Dropdown(
                        id='category-selector-' + pageNumber,
                        options=options,
                        value=table[0],
                        multi=False
                                )
    return category_selector





def getSelectorsForTab2(df, pageNumber):
    table = ['Кол-во структур, ед',
            'Всего кол-во сотрудников, чел',
            'Всего с профильным образованием',
            'Всего объeм финансирования, руб',
            'Расходы на мероприятия',
            'Расходы на адм функции',
            'Расходы на ремонт']
    

    county_options = []
    for el in np.append('Все округи', df['Округ'].unique()):
        county_options.append({'label': el, 'value': el})



    #county_options = np.append('Все округи', df['Округ'].unique())

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
                        value='Все регионы',
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

    table2 = ['Общественные объединения, включенные в реестр детских и молодeжных объединений, пользующихся государственной поддержкой',
            'Объединения, включенные в перечень партнеров органа исполнительной власти, реализующего государственную молодeжную политику',
            'Политические молодeжные общественные объединения',
            'Молодeжные патрули / добровольные молодeжные дружины']

    county_options = []
    for el in np.append('Все округи', df['Округ'].unique()):
        county_options.append({'label': el, 'value': el})



    region_options = []
    for el in np.append('Все регионы', df['Регион'].unique()):
        region_options.append({'label': el, 'value': el})


    special_options = []

    for key in table:
        special_options.append({'label': key, 'value': key})

    category_selector = dcc.Dropdown(
                        id='category-selector-' + pageNumber,
                        options=special_options,
                        value=table[0],
                        multi=False
                                )

    

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
                        value=['Все округи'],
                        multi=True
                                )


    region_selector = dcc.Dropdown(
                        id='region-selector-' + pageNumber,
                        options=region_options,
                        value=[''],
                        multi=True
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



def getSelectorForTab8(df, pageNumber):
    table, _ = getTables(pageNumber)
    options = []

    for el in table:
        options.append({'label': el, 'value': el})

    category_selector = dcc.Dropdown(
                        id='category-selector-' + pageNumber,
                        options=options,
                        value=table[0],
                        multi=False
                                )
    return category_selector
    
