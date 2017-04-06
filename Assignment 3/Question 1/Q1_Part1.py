from pandas import Series, DataFrame
from datetime import datetime as dt
import pandas as pd

data=pd.read_csv('C:/Users/ABC/DataAnalysis4Python_Spring17/Assignments/Assignment 3/Data/vehicle_collisions.csv', sep=',', parse_dates=['DATE'], skiprows=(1,1))
df=DataFrame(data, columns=['BOROUGH', 'DATE'])
df['MONTH']=data['DATE'].dt.month
df['YEAR']=data['DATE'].dt.year
#df.MONTH.value_counts().sort_index()

df_nyc['MANHATTAN']=df[['BOROUGH','MONTH']].loc[(df['YEAR'] == 2016)&(df['BOROUGH'] == 'MANHATTAN')].groupby(['MONTH']).count()
df_nyc['NYC']=df[['BOROUGH','MONTH']].loc[(df['YEAR'] == 2016)].groupby(['MONTH']).count()
#df_nyc.columns=['MANHATTAN','NYC']
df_nyc['PERCENTAGE']= df_nyc['MANHATTAN']/df_nyc['NYC']


df_nyc.to_csv('Q1_Part1Output.csv', sep=',', encoding='utf-8')
