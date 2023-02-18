from scripts.selectors import getSelectorsForTab2, getSelectorsForTab4

from dash import html
from dash import dcc
import dash_bootstrap_components as dbc


def getTab4(df, pageNumber):
    pageNumber = str(pageNumber)
    category_selector, county_selector, region_selector, type_selector, region_selector_vs1, region_selector_vs2 = getSelectorsForTab4(df, pageNumber)

    tab2 = [


        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col(
                        [
                            html.Div('Выберите категорию'),
                            html.Div(category_selector,
                                     style={'width': '75%',
                                            'margin-bottom': '40px',
                                            'margin-right': '10px'})

                        ], width={'size': 8}),

                    dbc.Col(
                        [
                            html.Div('Выберите значение'),
                            html.Div(type_selector,
                                     style={'width': '75%',
                                            'margin-bottom': '40px',
                                            'margin-right': '10px'})

                        ], width={'size': 8}),

                    ], style={'margin-top': '60px', 'margin-left': '80px'}),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div('Выберите округ'),
                                html.Div(county_selector,
                                         style={'width': '75%',
                                                'margin-bottom': '40px',
                                                'margin-right': '10px'}),
                            ], width={'size': 4}),

                        dbc.Col(
                            [
                                html.Div('Выберите регион'),
                                html.Div(region_selector,
                                         style={'width': '75%',
                                                'margin-bottom': '40px',
                                                'margin-right': '10px'}),
                            ], width={'size': 4}),
                    ], style={'margin-top': '60px', 'margin-left': '80px'})

                ]),
            dbc.Col(
                [
                    dbc.Col(
                        [
                            dcc.Graph(id='graph-' + pageNumber),
                        ], width={'size': 16})
                ], style={'margin-bottom': '40px'})

            ]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(id='graph-map-' + pageNumber),
                    ], width={'size': 16})
            ], style={'margin-bottom': '40px'}),

        
        dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div('Регион 1'),
                                html.Div(region_selector_vs1,
                                         style={'width': '75%',
                                                'margin-bottom': '40px',
                                                'margin-right': '10px'}),
                            ], width={'size': 4}),

                        dbc.Col(
                            [
                                html.Div('Регион 2'),
                                html.Div(region_selector_vs2,
                                         style={'width': '75%',
                                                'margin-bottom': '40px',
                                                'margin-right': '10px'}),
                            ], width={'size': 4}),
                    ], style={'margin-top': '60px', 'margin-left': '80px'}),


        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(id='graph-vs-' + pageNumber),
                    ], width={'size': 16})
            ], style={'margin-bottom': '40px'}),


        

    ]


    return tab2