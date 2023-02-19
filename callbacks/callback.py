from scripts.graphs import drawing_graphs, amount_by_county_p2, amount_by_region_p2, amount_by_county_p4, statistics_by_year
from scripts.graphs import amount_by_region_p4, region_comparison, region_comparison_2, draw_horizontal_graph
from scripts.map import building_map_by_region_p2, amount_by_region_map_p2


def first_tab(card_cat, df, county):
    df_map = amount_by_region_map_p2(df, card_cat)
    fig = building_map_by_region_p2(df_map, county)
    return fig


def second_tab(card_cat, type_cat, county, region, region1, region2, df, counties):
    df_map = amount_by_region_map_p2(df, f'{type_cat} ({card_cat})')
    fig2 = building_map_by_region_p2(df_map, counties)
    fig3 = draw_horizontal_graph(df)

    if region[0] == '':

        if 'Все округи' in county:
            fig1 = amount_by_county_p2(df, card_cat, 'ЦФО', all=True)

        else:
            fig1 = amount_by_county_p2(df, card_cat, county, all=False)

    else:
        if 'Все регионы' in region:
            fig1 = amount_by_region_p2(df, card_cat, region, all = True)
        
        else:
            fig1 = amount_by_region_p2(df, card_cat, region, all=False)

    fig4 = fig1
    if region1 != '' and region2 != '':
        fig4 = region_comparison_2(df, card_cat, region1, region2)

    return fig1, fig2, fig3, fig4


def fourth_tab(card_cat, type_cat, county, region, region1, region2, df, counties):
    df_map = amount_by_region_map_p2(df, f'{type_cat} ({card_cat})')
    fig2 = building_map_by_region_p2(df_map, counties)
    if region[0] == '':

        if 'Все округи' in county:
            fig1 = amount_by_county_p4(df, card_cat, 'ЦФО', all=True)

        else:
            fig1 = amount_by_county_p4(df, card_cat, county, all=False)

    else:
        if 'Все регионы' in region:
            fig1 = amount_by_region_p4(df, card_cat, region, all = True)
        
        else:
            fig1 = amount_by_region_p4(df, card_cat, region, all=False)

    fig3 = fig1
    if region1 != '' and region2 != '':
        fig3 = region_comparison(df, card_cat, region1, region2)

    return fig1, fig2, fig3


def eight_tab(df, card_cat):
    fig = statistics_by_year(df, card_cat)
    return fig