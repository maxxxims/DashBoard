from dash import html
from dash import dcc
import dash_bootstrap_components as dbc




def getTab0():
    hints = html.Datalist( id='hints-regions', children=[
                                html.Option(value="Example"),
                                html.Option(value="Kray"),
                                html.Option(value="Sgo")
                            ])

    tab0 = [
        html.Div(
            [
            html.H3('Главная страница'),
            html.Div('Здесь будет какая-то вводная информация про dashboard и все прочее')                
            ], style={'align' : 'center'}),
            

           ]

    return tab0