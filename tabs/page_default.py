from scripts.selectors import getSelectorsForTab1

from dash import html
from dash import dcc
import dash_bootstrap_components as dbc


def getTabDefault(pageNumber):
    
    tab1 = html.Div('Coming soon', style={'align': 'center'})

    return tab1