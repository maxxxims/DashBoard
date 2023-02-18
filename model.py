import numpy as np
import pandas as pd

from dash import dcc



df2 = pd.read_csv("data/Р2.csv")


#print(df2['Регион'].unique())

# from scripts.graphs import amount_by_county_p2

# fig = amount_by_county_p2(df2, 'Всего кол-во сотрудников, чел', 'ЦФО', all=False)

# fig.show()