import pandas as pd
import numpy as np

df_item_categories = pd.read_csv('../../data/external/item_categories.csv')
df_items = pd.read_csv('../../data/external/items.csv')
df_sales = pd.read_csv('../../data/external/sales_train.csv')
df_shops = pd.read_csv('../../data/external/shops.csv')
df_test = pd.read_csv('../../data/external/test.csv')

df_train = df_sales.merge(df_shops, on = 'shop_id', how = 'left')
df_train = df_train.merge(df_items, on = 'item_id', how ='left')
df_train = df_train.merge(df_item_categories, on = 'item_category_id', how = 'left')

df_train.to_csv('../../data/processed/train.csv', index = False)