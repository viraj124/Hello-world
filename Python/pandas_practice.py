import pandas as pd
import numpy as np

chipo=pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv',sep='\t')
print(chipo['quantity'])
print(chipo.columns)
c=chipo.groupby('item_name')
c=c.sum()
c=c.sort_values(['quantity'],ascending=False)
print(c.head(1))

c=chipo.groupby('choice_description')
c=c.sum()
c=c.sort_values(('quantity'),ascending=False)
print(c.head(1))

c=chipo['quantity']
c=c.sum()
print(c)

convert=lambda x: float(x[1:])
chipo.item_price.apply(convert)
print(chipo.head())

cost=chipo.quantity*chipo.item_price


c=chipo.item_name.value_counts().count()
print(c)
