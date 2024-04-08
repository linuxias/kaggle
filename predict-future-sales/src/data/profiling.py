import pandas as pd
from ydata_profiling import ProfileReport
from pydantic_settings import BaseSettings

df = pd.read_csv('../../data/processed/train.csv')
pr = df.profile_report(title='Profiling Report')
pr.to_file('../../reports/profiling_report.html')