import dash
from dash import html, dash_table, ctx
from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from layout import getLayOut
from model import df2, df4, counties
from callbacks.callback import first_tab, second_tab, fourth_tab


app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = getLayOut(df2.getDataSet())


@app.callback(
    Output('container-button', 'children'),
    Input('refresh-data', 'n_clicks'),
)
def update_output(n_clicks):
    if "refresh-data" == ctx.triggered_id:
        df2.setDataSet()
        return 'Ваши данные успешно обновленны, пожалуйста, обновите страницу'

    else:
        return 'Нажмите, чтобы обновить данные'
    


@app.callback(
    Output(component_id='graph-2', component_property='figure'),
    Output(component_id='graph-map-2', component_property='figure'),
    Output(component_id='graph-2-2', component_property='figure'),
    Output(component_id='graph-vs-2', component_property='figure'),
    [Input(component_id='category-selector-2', component_property='value'),
    Input(component_id='county-selector-2', component_property='value'),
    Input(component_id='region-selector-2', component_property='value'),
    Input(component_id='type-selector-2', component_property='value'),
    Input(component_id='region-selector-vs1-2', component_property='value'),
    Input(component_id='region-selector-vs2-2', component_property='value'),
    ]    
)
def update_second_tab(card_cat, county, region, type, region1, region2):
    return second_tab(card_cat, type, county, region, region1, region2, df2.getDataSet(), counties)


@app.callback(
    Output(component_id='graph-4', component_property='figure'),
    Output(component_id='graph-map-4', component_property='figure'),
    Output(component_id='graph-vs-4', component_property='figure'),
    [Input(component_id='category-selector-4', component_property='value'),
    Input(component_id='county-selector-4', component_property='value'),
    Input(component_id='region-selector-4', component_property='value'),
    Input(component_id='type-selector-4', component_property='value'),
    Input(component_id='region-selector-vs1-4', component_property='value'),
    Input(component_id='region-selector-vs2-4', component_property='value'),
    ]    
)
def update_fourth_tab(card_cat, county, region, type, region1, region2):
    return fourth_tab(card_cat, type, county, region, region1, region2, df4.getDataSet(), counties)

if __name__ == '__main__':
    app.run_server(debug=True)