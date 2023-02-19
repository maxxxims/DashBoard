from dash import html
from dash import dcc
import dash_bootstrap_components as dbc


def getTab0():

    tab0 = [
                dbc.Row(
                    html.H1('Наглядно и точка.', style={'font-size': '380px', 'opacity': '.5', 'color': '#897AD6', 'background': '-webkit-linear-gradient(#897AD6, #8eaf0c)',
                                                          '-webkit-background-clip': 'text',
                                                          '-webkit-text-fill-color': 'transparent'})
                ),
           ]
    return tab0