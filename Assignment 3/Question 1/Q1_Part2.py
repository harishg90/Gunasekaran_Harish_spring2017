from pandas import Series, DataFrame
import pandas as pd
import numpy as np

data=pd.read_csv('C:/Users/ABC/DataAnalysis4Python_Spring17/Assignments/Assignment 3/Data/vehicle_collisions.csv', sep=',', skiprows=(1,1))
df=DataFrame(data, columns=['BOROUGH', 'VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE'])
df['VEHICLE 1 TYPE'] = df['VEHICLE 1 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)
df['VEHICLE 2 TYPE'] = df['VEHICLE 2 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)
df['VEHICLE 3 TYPE'] = df['VEHICLE 3 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)
df['VEHICLE 4 TYPE'] = df['VEHICLE 4 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)
df['VEHICLE 5 TYPE'] = df['VEHICLE 5 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)
df['TOTAL'] = df['VEHICLE 1 TYPE']+df['VEHICLE 2 TYPE']+df['VEHICLE 3 TYPE']+df['VEHICLE 4 TYPE']+df['VEHICLE 5 TYPE']

df['ONE VEHICLE INVOLVED']= np.where(df['TOTAL'] == 1, 1,0)
df['TWO VEHICLE INVOLVED']= np.where(df['TOTAL'] == 2, 1,0)
df['THREE VEHICLE INVOLVED']= np.where(df['TOTAL'] == 3, 1,0)
df['MORE VEHICLES INVOLVED']= np.where(df['TOTAL'] >= 4, 1,0)
df=df.groupby('BOROUGH').sum()

df=DataFrame(df,columns=['ONE VEHICLE INVOLVED','TWO VEHICLE INVOLVED','THREE VEHICLE INVOLVED','MORE VEHICLES INVOLVED'])
df.to_csv('Q1_Part2Output.csv', sep=',', encoding='utf-8')
df.head()