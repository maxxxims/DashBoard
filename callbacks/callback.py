from scripts.graphs import drawing_graphs, amount_by_county_p2, amount_by_region_p2
from scripts.map import building_map_by_region_p2, amount_by_region_map_p2


def first_tab(card_cat, table_column, filter, df, table):
    if table_column == '':
        fig = drawing_graphs(card_cat, df)


    elif table_column != '' and filter == '':
        fig = drawing_graphs(card_cat, df)


    elif table_column != '' and  filter != '':
        fig = drawing_graphs(card_cat, df=df[(df[table_column] == filter)])
    

    else:
        fig = drawing_graphs(card_cat, df)


    if table_column == '':
        return fig, []
    else:
        return fig, table[table_column]


def second_tab(card_cat, type_cat, county, region, df, counties):
    df_map = amount_by_region_map_p2(df, f'{type_cat} ({card_cat})')
    fig2 = building_map_by_region_p2(df_map, counties)

    if region == '':

        if county == 'Все округи':
            fig1 = amount_by_county_p2(df, card_cat, 'ЦФО', all=True)

        else:
            fig1 = amount_by_county_p2(df, card_cat, county, all=False)

    else:
        if region == 'Все регионы':
            fig1 = amount_by_region_p2(df, card_cat, region, all = True)
        
        else:
            fig1 = amount_by_region_p2(df, card_cat, region, all=False)

    return fig1, fig2