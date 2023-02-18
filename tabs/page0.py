from dash import html
from dash import dcc
import dash_bootstrap_components as dbc




def getTab0():
    tab0 = [
        html.Div(
            [
            html.H3('Главная страница'),
            html.Div('Здесь будет какая-то вводная информация про dashboard и все прочее')                
            ], style={'align' : 'center'}),
            

           ]

    return tab0