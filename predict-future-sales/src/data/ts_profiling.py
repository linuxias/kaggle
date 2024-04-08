import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('../../data/processed/train.csv', index_col = [0])
pr = ProfileReport(df, title='Profiling Report', tsmode = True, sortby = "date_block_num")
pr.to_file('../../reports/ts_profiling_report.html')