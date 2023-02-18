from tabs.page1 import getTab1
from tabs.table import getTable
from tabs.page0 import getTab0
from tabs.page2 import getTab2
from dash import html
import dash_bootstrap_components as dbc
from tabs.page4 import getTab4

def getLayOut(df2):
    layout = html.Div(
        [
        dbc.Row(html.H1("Torch-ки"),
                style={'margin-bottom': '40px'}),

        html.Div([
            html.Button('Обновить', id='refresh-data', n_clicks=0),
            html.Div(id='container-button',
             children='Нажмите, чтобы обновить данные')

        ], style={'align': 'left'}),

        dbc.Tabs(
            [
                dbc.Tab(getTab0(), label='Начальная странца'),
                dbc.Tab(getTab1(1), label='Страница 1'),
                dbc.Tab(getTab2(df2,2), label='Страница 2'),
                dbc.Tab(getTab1(3), label='Страница 3'),
                dbc.Tab(getTab4(df2, 4), label='Страница 4'),
                dbc.Tab(getTab1(5), label='Страница 5'),
                dbc.Tab(getTab1(6), label='Страница 6'),
                dbc.Tab(getTab1(7), label='Страница 7'),
                dbc.Tab(getTab1(8), label='Таблица')
            ]),
        
        ],style={'margin-left': '200px', 'margin-right': '200px' },
                    )

    return layout