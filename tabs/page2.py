from scripts.selectors import getSelectorsForTab2

from dash import html
from dash import dcc
import dash_bootstrap_components as dbc


def getTab2(df, pageNumber):
    pageNumber = str(pageNumber)
    category_selector, county_selector, region_selector = getSelectorsForTab2(df, pageNumber)

    tab2 = [
        dbc.Row(
            [
        
            dbc.Col(
                [
                html.Div('Выберите категорию'),
                html.Div(category_selector,
                        style={'width': '400px',
                                'margin-bottom': '40px'}),
                ], width={'size': 4}),

            

            ]),
            
        dbc.Row(
            dbc.Col(
                dbc.Col(
                [
                html.Div('Выберите округ'),
                html.Div(county_selector,
                        style={'width': '400px',
                                'margin-bottom': '40px'}),
                ], width={'size': 4})
            )
        ),

        dbc.Row(dbc.Col(
            [
                html.Div('Выберите регион'),
                html.Div(region_selector,
                        style={'width': '400px',
                                'margin-bottom': '40px'}),
            ], width={'size': 4})),

        dbc.Row(
            [
            dbc.Col(
                [
                dcc.Graph(id='graph-' + pageNumber),
                ], width={'size': 16})
            ], style={'margin-bottom': '40px'}),

    ]

    return tab2