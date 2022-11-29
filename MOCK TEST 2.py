# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 12:11:12 2022

@author: dharm
"""

# DATA RESOURCE LINK
#https://www2.census.gov/programs-surveys/popest/tables/2010-2019/counties/totals/co-est2019-annres.xlsx

import numpy as np
import pandas as pd
a = pd.read_csv('C:/Users/dharm/Downloads/co-est2019-annres.csv')
df = pd.DataFrame({'value': [308745538, 308758105, 309321666, 311556874, 313830990,315993715 ,318301008 ,320635163 ,322941311 , 324985539,326687501 ,328239523]},
              index=pd.DatetimeIndex(['2010', '2011', '2012', '2013',
                                      '2014', '2015', '2016', '2017',
                                      '2018', '2019', '2020']))


pv = pd.pivot_table(df, index=df.index.month, columns=df.index.year,
                    values='value', aggfunc='sum')
