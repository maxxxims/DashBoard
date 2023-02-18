from dash import html, dash_table


def getTable(df):
    tab2 = [html.Div(
        [
            html.H2("Таблица", style = {'text-align': 'center'}),

            dash_table.DataTable(
                df.to_dict('records'),
                [{"name": i, "id": i} for i in df.columns],
                style_table={'height': '300px', 'overflowY': 'auto'},
                page_size= 20,
                style_header={ 'border': '1px solid black' },
                style_cell={ 'border': '1px solid grey' },
                )
        ]
        #style = {'margin-top': '80px', 'margin-left': '80px', 'margin-right': '80px'}
                )]

    return tab2