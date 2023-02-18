from scripts.graphs import drawing_graphs, amount_by_county_p2, amount_by_region_p2


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


def second_tab(card_cat, county, region, df):

    # category = card_cat.split('(')[1]
    # category = category.replace(')', '')
    # print(category)

    if region == '':

        if county == 'Все округи':
            fig = amount_by_county_p2(df, card_cat, 'ЦФО', all=True)

        else:
            fig = amount_by_county_p2(df, card_cat, county, all=False)

    else:
        if region == 'Все регионы':
            fig = amount_by_region_p2(df, card_cat, region, all = True)
        
        else:
            fig = amount_by_region_p2(df, card_cat, region, all=False)

    return fig