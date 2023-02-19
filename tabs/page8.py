from scripts.selectors import getSelectorForTab8
from scripts.analytic import first_page
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc



def getTab8(df, pageNumber):
    pageNumber = str(pageNumber)

    category_selector = getSelectorForTab8(df, pageNumber)
    tab2 = [


        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Row(
                        [
                            html.Div('Выберите категорию'),
                            html.Div(category_selector,
                                     style={'width': '100%',
                                            'margin-bottom': '40px',
                                            'margin-right': '10px'})

                        ]),

                    ],style={'box-shadow': 'rgba(0, 0, 0, 0.24) 0px 3px 8px', 'margin-bottom': '10px',
                                            'background-color': '#f9f9f9',
                                            'padding': '6px',
                                            'border-radius': '15px',
                                            'width': '63%', 'position': 'absolute', 'top': '260px', 'left': '335px', 'width': '740px', 'height': '480px',
                            }),
                ]),
            dbc.Col(
                [
                    dbc.Col(
                        [
                            dcc.Graph(id='graph-' + pageNumber, style={'height': '480px'})
                        ])
                ], style={'box-shadow': 'rgba(0, 0, 0, 0.24) 0px 3px 8px',
                                            'background-color': '#f9f9f9',
                                            'border-radius': '15px',
                                            'position': 'absolute', 'top': '260px', 'left': '1100px', 'width': '1100px'
                          })

            ]),
    ]
    return tab2
