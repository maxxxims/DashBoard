import plotly.express as px
import pandas as pd


def first_page():
    feature_importance = [15.24905223, 25.63748124, 13.32143107, 28.8864013, 16.90563416]
    feature_names = ['Бюджет СРФ, руб', 'Бюджет МО, руб', 'Кол-во грантов', 'Бюджет грантов, руб',
                    'Количество общественных объединений'] 

    data={'feature_names':feature_names,'feature_importance':feature_importance}

    fi_df = pd.DataFrame(data)


    fi_df.sort_values(by=['feature_importance'], ascending=True,inplace=True)

    fig = px.bar(
    data_frame = fi_df,
    y = 'feature_names',
    x = 'feature_importance',
    barmode = 'group',
    title='Влияние признака на количество вовлеченной молодежи',
    color_discrete_sequence=['#897AD6', '#897AD6', '#897AD6', '#897AD6', '#897AD6']
    )

    return fig