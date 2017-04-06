from pandas import Series, DataFrame
import pandas as pd
import numpy as np

dataset=pd.read_csv('C:/Users/ABC/DataAnalysis4Python_Spring17/Assignments/Assignment 3/Data/cricket_matches.csv', sep=',')[['home','result','winner','innings1','innings1_runs','innings2','innings2_runs']]
df = DataFrame(dataset[dataset.apply(lambda x: x['home'] == x['winner'], axis = 1)])
df['winner score'] = np.where(df['winner']==df['innings1'],df['innings1_runs'],df['innings2_runs'])
#df['winner sre'] = df[df.apply(lambda x: x['innings1_runs'] if x['home'] == x['innings1'] else x['innings2_runs'])]
#df2 = df[df.apply(lambda x: x['innings1_runs'] if x['winner'] == x['innings1'] else x['innings2_runs'])]
df = DataFrame(df.groupby('home')['winner score'].mean())
df
df.to_csv('Question3Output.csv', sep=',', encoding='utf-8')