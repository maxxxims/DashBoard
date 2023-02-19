from scripts.selectors import getSelectorsForTab2, getSelectorsForTab4, getSelectorsForTab1
from scripts.analytic import first_page
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc



def getTab1(df, pageNumber):
    pageNumber = str(pageNumber)

    category_selector = getSelectorsForTab1(df, pageNumber)
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
                                            'width': '63%', 'position': 'absolute', 'top': '260px', 'left': '335px', 'width': '740px', 'height': '100px',
                            }),
                ]),
            dbc.Col(
                [
                    dbc.Col(
                        [
                            dcc.Graph(
                                figure=first_page(), id='analytic-' + pageNumber, style={'height': '480px'})
                        ])
                ], style={'box-shadow': 'rgba(0, 0, 0, 0.24) 0px 3px 8px',
                                            'background-color': '#f9f9f9',
                                            'border-radius': '15px',
                                            'position': 'absolute', 'top': '260px', 'left': '1100px', 'width': '1100px'
                          })

            ]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(id='graph-map-' + pageNumber, style={'height': '500px'}),
                    ], style={ 'box-shadow': 'rgba(0, 0, 0, 0.24) 0px 3px 8px', 'margin-bottom': '10px',
                                            'background-color': '#f9f9f9',
                                            'padding': '6px',
                                            'border-radius': '15px',
                                            'position': 'absolute', 'top': '770px', 'left': '325px', 'width': '1878px',}),
            ],),
########################################################################################################################
        # dbc.Row(
        #     [

        #         dbc.Row(
        #             [
        #                 dbc.Col(
        #                     [
        #                         html.Div('Регион 1'),
        #                         html.Div(region_selector_vs1,
        #                                  style={'width': '75%',
        #                                         'margin-bottom': '40px',
        #                                         'margin-right': '10px'}),
        #                     ], width={'size': 4}),

        #                 dbc.Col(
        #                     [
        #                         html.Div('Регион 2'),
        #                         html.Div(region_selector_vs2,
        #                                  style={'width': '75%',
        #                                         'margin-bottom': '40px',    
        #                                         'margin-right': '10px'}),
        #                     ], width={'size': 4}),
        #             ], style={'margin-top': '60px', 'margin-left': '80px', 'position': 'absolute', 'top': '1500px'}),


        #         dbc.Col(
        #             [
        #                 dcc.Graph(id='graph-vs-' + pageNumber)
        #             ], style={'position': 'absolute', 'top': '1700px', 'left': '525px', 'width': '1440px', 'z-index': 0, 'box-shadow': 'rgba(0, 0, 0, 0.24) 0px 3px 8px', 'margin-bottom': '10px',
        #                                     'background-color': '#f9f9f9',
        #                                     'padding': '6px',
        #                                     'border-radius': '15px'}),
        #     ],),




    ]
    return tab2
