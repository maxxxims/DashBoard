from tabs.page_default import getTabDefault
from tabs.page1 import getTab1
from tabs.table import getTable
from tabs.page0 import getTab0
from tabs.page2 import getTab2
from tabs.page8 import getTab8
from dash import html, dcc
import dash_bootstrap_components as dbc
from tabs.page4 import getTab4





def getLayOut(df1, df2):
    tabs_styles = {
        'height': '44px',
    }
    tab_style = {
        'color': "#897AD6", 'width': '120px',
        'box-shadow': 'rgba(0, 0, 0, 0.24) 0px 3px 8px',
        'padding': '6px',
        'fontWeight': 'bold',
        'border-radius': '60px',
        'margin-right': '33px',
        'background-color': '#f9f9f9',
        # 'border': '8px',
        'borderTop': '1px solid #897AD6',
        'borderBottom': '1px solid #897AD6',
        'borderLeft': '1px solid #897AD6',
        'borderRight': '1px solid #897AD6',
    }

    tab_selected_style = {
        'borderTop': '1px solid #897AD6',
        'borderBottom': '1px solid #897AD6',
        'borderLeft': '1px solid #897AD6',
        'borderRight': '1px solid #897AD6',
        'background-color': '#897AD6',
        'color': 'white',
        'padding': '6px',
        'border-radius': '60px',
        'width': '6%',
        'margin-right': '33px',
        'box-shadow': 'rgba(0, 0, 0, 0.24) 0px 3px 8px',
    }

    layout = html.Div(
        [
        dbc.Row(
            [
                dbc.Col(html.H1("Росмолодежь аналитика"), width={'size': 11}),
                dbc.Col(
                    html.Div(
                        [
                            dbc.Button("Обновить", className="me-1", id='refresh-data', n_clicks=0, style={'color': "#897AD6", 'width': '100px', 'height': '44px', 'border-radius': '60px', 'box-shadow': '#897AD6 0px 3px 8px',
                                            'background-color': '#f9f9f9'}),
                            html.Div(id='container-button',
                            children='')

                        ], style={'margin-top': '15px', 'position': 'absolute', 'top': '116px', 'left': '2080px', }),)
            ], style={'margin-bottom': '20px', 'margin-top': '50px'}),

        dcc.Tabs(
            [
                dcc.Tab(getTab0(), label='Начало', style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(getTab1(df1,1), label='Затраты', style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(getTab2(df2,2), label='Структуры', style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(getTabDefault(3), label='Просмотры', style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(getTab4(df2, 4), label='Образование', style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(getTabDefault(5), label='Гос Органы', style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(getTabDefault(6), label='Форумы', style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(getTabDefault(7), label='Волонтерство', style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(getTab8(df2, 8), label='Статистика', style=tab_style, selected_style=tab_selected_style)
            ], style=tabs_styles),


        ],style={'margin-left': '320px', 'margin-right': '320px'})


    return layout