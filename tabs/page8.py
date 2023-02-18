from dash import html
from dash import dcc
import dash_bootstrap_components as dbc


def getTab8(df, pageNumber):
    table = []

    options = []
    for el in table:
        options.append({'label': el, 'value': el})


    category_selector = dcc.Dropdown(
                        id='category-selector-' + pageNumber,
                        options=options,
                        value='',
                        multi=False
                                )

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

                        ], width={'size': 8})

                    ], style={'margin-top': '60px', 'margin-left': '80px'}),
            

                ]),

            dbc.Col(
                [
                    dbc.Col(
                        [
                            dcc.Graph(id='graph-' + pageNumber),
                        ], width={'size': 16})
                ], style={'margin-bottom': '40px'})

            ])

    ]
    
    return tab2